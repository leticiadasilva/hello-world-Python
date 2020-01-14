# Pede para o usuário inserir o primeiro valor da subtração (input significa entrada de dados). Recebe os valores em formato de string.
# Atribui o valor digitado para a variável "primeiro_valor"
primeiro_valor = input("Digite o primeiro valor: ")

# Pede para o usuário inserir o segundo valor da subtração
# Atribui o valor digitado para a variável "segundo_valor"
segundo_valor = input("Digite o segundo valor: ")

# Faz a subtração do primeiro_valor - segundo_valor e o atribbui a variável "calculo". Atenção: o "int" antes 
# das variáveis serve para transformá-las em números inteiros e possibilitar que o cálculo seja feito.
calculo = int(primeiro_valor) - int(segundo_valor)

# Pede para imprimir (função print) o texto "SUBTRAÇÃO = " e o concatena (concatena significa juntar algo) com a variável calculo.
# Repare que a variável soma precisa ser transformada novamente para string (str) para ser impressa junto com o texto digitado.
print ("SUB = ", str(calculo))


primeiro_valor = input("Digite o primeiro valor: ")
segundo_valor = input("Digite o segundo valor: ")

calculo = int(primeiro_valor) - int(segundo_valor)

print ("SUB = ", str(calculo))


