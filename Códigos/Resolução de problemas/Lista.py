'''Escreva uma lista de frutas com 3 frutas. Adicione “kiwi” nesta lista. Escreva uma lista de vegetais com 5 itens. Apague o item do meio. Junte as duas listas em uma lista só, chamada “feira”.'''

frutas = ['banana', 'uva','morango']
frutas.append('kiwi')
verdura = ['alface','rúcula', 'hortelã', 'agrião', 'alface americana' ]
del verdura[2]
feira = [frutas + verdura]
print(feira)