import pyodbc
from config import database
from logs import logging


class DBManager:
    def __init__(self):
        self.connection = pyodbc.connect(
            driver=database('db_driver'),
            server=database('db_server'),
            database=database('db_name'),
            uid=database('db_user'),
            pwd=database('db_pass')
        )
    
    def call_sp(self, procedure, params=None):
        cursor = self.connection.cursor()
        try:
            if params is None:
                cursor.execute(f"{{CALL {procedure}}}")
            else:
                cursor.execute(f"{{CALL {procedure} ({','.join(['?'] * len(params))})}}", params)

            self.connection.commit()
            return True
        except Exception as e:
            logging.error(f"Error ejecutando SP: {e}")
            raise
    
    def get_all_data(self, table):
        return self.query(f"SELECT * FROM {table}")
    
    def query(self, query):
        cursor = self.connection.cursor()
        
        try:
            cursor.execute(query)
            columns = [column[0] for column in cursor.description]  # Obtener los nombres de las columnas
            results = cursor.fetchall()
            # Convertir los resultados a una lista de diccionarios
            return [dict(zip(columns, row)) for row in results]
        except Exception as e:
            logging.error(f"Error: {e}")
            raise