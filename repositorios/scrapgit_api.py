# -*- coding: utf-8 -*-
import requests
import json
import pandas as pd
import os, sys

# MONGODB
from pymongo import MongoClient
client = MongoClient('localhost')
db = client['db_repositorios']
col = db['repositorios_repositorio']

headers = {
	"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
}

repositorios_git = []

# Documentacion del API: https://api.github.com/
endpoint = "https://api.github.com/users/Josheriff/repos?" #"https://api.github.com/users/Josheriff/repos?"


response = requests.get(endpoint)

# RESPUESTA ESTA EN FORMATO JSON
repositorios = response.json() # puedo utilizar la libreria json para ver de la mejor manera
for repositorio in repositorios:
    #print(json.dumps(response.json(), indent=4))
    itulo = repositorio["name"].replace('-', ' ').replace('/', '').replace('_', ' ').strip()
    descripcion = repositorio["description"]  # .replace('-', '').replace('/', '').replace('_', ' ').strip()
    star = repositorio["stargazers_count"]
    fork = repositorio["forks_count"]
    fecha_creacion = repositorio["created_at"]
    fecha_actualizacion = repositorio["updated_at"]
    url_commits = repositorio["commits_url"].replace('{/sha}', '').strip()
    url_colaboradores = repositorio["contributors_url"]
    url_lenguajes = repositorio["languages_url"]
    url_repositorio = repositorio["svn_url"]

    col.update_one(
        {
            "titulo": titulo
            # "descripcion": descripcion
        }, {
            "$set": {
                "descripcion": descripcion,
                "star": star,
                "fork": fork,
                "fecha_creacion": fecha_creacion,
                "fecha_actualizacion": fecha_actualizacion,
                "url_commits": url_commits,
                "url_colaboradores": url_colaboradores,
                "url_lenguajes": url_lenguajes,
                "url_repositorio": url_repositorio,
                "titulo": titulo
            }
        }, upsert=True)  # upsert --> Operación de INSERCIÓN en caso de no existir un documento
    # que cumpla con mi condición. Y Operación de ACTUALIZACIÓN en caso de que
    # exista un documento que cumpla con mi condición.

#df = pd.DataFrame(repositorios_git)
#print(df)
#df.to_csv("repositorios_github4.csv")
    #print(json.dumps(response.json(), indent=4))