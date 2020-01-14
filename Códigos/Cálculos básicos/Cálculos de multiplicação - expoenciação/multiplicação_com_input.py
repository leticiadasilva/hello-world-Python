# Pede para o usuário inserir o primeiro valor da multiplicação (input significa entrada de dados). Recebe os valores em formato de string.
# Atribui o valor digitado para a variável "valor_1"
valor_1 = input ("Digite o primeiro valor: ")

# Pede para o usuário inserir o segundo valor da multiplicação
# Atribui o valor digitado para a variável "valor_2"
valor_2 = input ("Digite o segundo valor: ")

# Multiplica valor_1 pelo valor_2 e armazena o resultado na variável "prod". Atenção: o "int" antes 
# das variáveis serve para transformá-las em números inteiros e possibilitar que a conta seja feita (pois quando o dado vem através de um input, ele está no formato de string).
prod = int(valor_1) * int(valor_2)

# Pede para imprimir (função print) o texto "PRODUTO = " e o concatena (concatena significa juntar algo) com a variável prod.
# Repare que a variável prod precisa ser transformada novamente para string (str) para ser impressa junto com o texto digitado.
print ("PRODUTO = ", str(prod))


valor_1 = input ("Digite o primeiro valor: ")
valor_2 = input ("Digite o segundo valor: ")

prod = int(valor_1) * int(valor_2)

print ("PRODUTO = ", str(prod))
