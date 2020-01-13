# Pede para o usuário inserir o primeiro valor da soma (input significa entrada de dados). Receve os valores em formato de string.
# Atribui o valor digitado para a variável "valor_1"
valor_1 = input ("Digite o primeiro valor: ")

# Pede para o usuário inserir o segundo valor da soma
# Atribui o valor digitado para a variável "valor_2"
valor_2 = input ("Digite o segundo valor: ")

# Faz o cálculo do valor_1 + valor_2 e o atribbui a variável "soma". Atenção: o "int" antes 
# das variáveis serve para transformá-las em números inteiros e possibilitar que o cálculo seja feito.
soma = int(valor_1) + int(valor_2)

# Pede para imprimir (função print) o texto "SOMA = " e o concatena (concatena significa juntar algo) com a variável soma.
# Repare que a variável soma precisa ser transformada novamente para string (str) para ser impressa.
print ("SOMA = ", str(soma))


valor_1 = input ("Digite o primeiro valor: ")
valor_2 = input ("Digite o segundo valor: ")
soma = int(valor_1) + int(valor_2)
print ("SOMA = ", str(soma))
