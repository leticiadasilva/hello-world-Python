'''Faça um programa que pergunte a idade e calcule em que faixa escolar a pessoa está (ensino fundamental, médio e graduação)'''

idade = int(input("Qual é a sua idade? "))

if idade >= 10 < 14:
    print ("Ensino Fundamental")
elif idade >= 15 < 18:
    print ("Ensino Médio")
else:
    print ("Graduação")