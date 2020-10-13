lista = ['5',7,'Ramones', '9']

print(f'lista sem alteração: {lista}')

# metodo pop remove o ultimo item da lista
lista.pop()
print(f'sem o ultimo item da lista: {lista}')

# metodo pop pode remover também um elemento pelo index da lista
lista.pop(2)
print(f'removendo também o elemento 2 da lista: {lista}')