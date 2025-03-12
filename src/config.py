import json
import os
import sys
import db

# Determina la ruta base
if getattr(sys, 'frozen', False):
    # Si está ejecutándose como un ejecutable
    base_path = os.path.dirname(sys.executable)
else:
    # Si está ejecutándose desde el código fuente
    base_path = os.path.dirname(__file__)

config_path = os.path.join(base_path, 'config.json')

with open(config_path,encoding='utf-8') as f:
    config = json.load(f)

def app(name):
    app = {
        "name":"SAViD",
        "fullname":"Sistema de Análisis y Verificación de Dietas",
        "version":"1.3"
    }
    return app[name]

def database(name):
    return db.db()[name]

def outlook(name):
    return config['outlook'][name]