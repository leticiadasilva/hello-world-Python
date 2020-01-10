# coding: utf-8
# Fonte: https://www.imdb.com/interfaces/
import json

arquivo = "gameofthrones.json"

with open(arquivo) as arquivo_json:
    lista_titulos = json.load(arquivo_json)
    for linha in lista_titulos:
        print("Título principal: {}".format(linha['primaryTitle']))
        print("Título original: {}".format(linha['originalTitle']))
        print("Ano de lançamento: {}".format(linha['startYear']))
        print("-----")
