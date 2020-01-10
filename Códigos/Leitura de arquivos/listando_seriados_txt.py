# coding: utf-8

arquivo = "seriados.txt"

with open(arquivo, "r") as arq:
    num_linha = 1
    for linha in arq:
        print("Linha {} ==> {}".format(num_linha, linha))
        num_linha += 1
