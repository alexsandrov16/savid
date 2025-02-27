import json

with open('config.json',encoding='utf-8') as f:
    config = json.load(f)

def app(name):
    return config['app'][name]

def database(name):
    return config['database'][name]

def outlook(name):
    return config['outlook'][name]