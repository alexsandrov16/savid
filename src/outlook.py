from datetime import datetime
from database import DBManager
from config import outlook
import os, re, pywintypes, pythoncom
import win32com.client
import logs,logging

class OutlookClient:
    def __init__(self):
        # Inicializar COM en el hilo actual
        pythoncom.CoInitialize()

        self.find=False

        try:
            self.outlook = win32com.client.Dispatch("Outlook.Application")
            self.mapi = self.outlook.GetNamespace("MAPI")
            self.account = self.mapi.Folders[outlook('user_mail')]
        except pythoncom.com_error as error:
            logging.error(f"Error al inicializar Outlook: {error.excepinfo[2]}")
            raise
        
    def __del__(self):
        # Limpieza de recursos COM
        try:
            if hasattr(self, 'outlook'):
                self.outlook.Quit()
            pythoncom.CoUninitialize()
        except Exception as e:
            logging.error(f"Error en limpieza: {str(e)}")

    def get_emails(self, subject=None):
        emails = []
        
        #Llama a la base de datos
        db = DBManager()

        # Obtener la fecha más reciente de la base de datos
        result = db.query(
            'SELECT TOP 1 fecha_correo FROM dietas ORDER BY fecha_correo DESC;'
        )

        if result:
            fecha_correo=result[0]['fecha_correo']
            
        else:
            fecha_correo=datetime(2023, 10, 2, 12, 0, 0)

        # Itera sobre todas las carpetas de la cuenta
        for folder in self.account.Folders:
            if folder.Name == outlook('folder'):
                self.find = True
                
                # Iterar sobre los correos del buzón
                for message in folder.Items:

                    #if hasattr(message, 'ReceivedTime')==True:
                    #else:
                    #    logging.error(f"Propiedad 'ReceivedTime' indefinida en el objeto OutlookMessage")

                    try:
                        convert_time = datetime(*message.ReceivedTime.timetuple()[:6])
                        if message.Subject == subject and convert_time > fecha_correo:
                            # Expresión regular para extraer la información deseada
                            regex = r"En fecha (\d{2}/\d{2}/\d{4}) (.+?) ha realizado una transferencia desde su cuenta (\d{16}) hacia la cuenta (\d{16}) por un importe de ([\d,.]+) con referencia (BR\w+)"
                            
                            coincidencias = re.search(regex, message.Body)
                            if coincidencias:
                                try:
                                    # Extraer información
                                    fecha = coincidencias.group(1)
                                    nombre = coincidencias.group(2).strip()
                                    cuenta_origen = coincidencias.group(3)
                                    cuenta_destino = coincidencias.group(4)
                                    importe = coincidencias.group(5)
                                    referencia = coincidencias.group(6)
                                    
                                    # Validar formato de fecha
                                    fecha_datetime = datetime.strptime(fecha, "%d/%m/%Y")
                                    fecha_formateada = fecha_datetime.strftime("%Y-%m-%d")
                                    
                                    # Insertar en base de datos
                                    db.call_sp('sp_InsertarDieta', [
                                        referencia,
                                        cuenta_origen,
                                        cuenta_destino,
                                        importe,
                                        fecha_formateada,
                                        nombre,
                                        convert_time
                                    ])
                                except Exception as e:
                                    logging.error(f"Error al procesar correo: {str(e)}")
                                    raise
                    except Exception as e:
                        logging.error(f"Error al procesar mensaje: {str(e)}")
                        continue
                
                break
        
        if not self.find:
            mnsg = f"No se encontró dentro de Outlook la carpeta: {outlook('folder')}"
            logging.critical(mnsg)
            raise Exception(mnsg)


def sendMailData():
    try:
        OutlookClient().get_emails(outlook('subject'))
        DBManager().call_sp('sp_ActualizaDietasPendientes')
        DBManager().call_sp('sp_ActualizaDietasPagadas')
    except:
        raise

