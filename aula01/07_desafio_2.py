# 1. Pergunte ao usuário em qual cidade e o estado em que ele(a) mora
nome = input('Qual seu nome? \n')
cidade = input('Em que cidade você mora?\n')
estado = input('Em que estado você mora?\n')
# 2. Imprima uma mensagem diga a cidade em que o usuário mora. 
#    O nome da cidade deve estar todo em letras maiúsculas.
frase = nome + ' mora em ' + cidade.upper() + '.'
print(frase)

# 3. Imprima uma mensagem diga o estado em que o usuário mora. 
#    O nome do estado deve estar todo em letras maiúsculas.
#    Utilize uma forma de formatação de string diferente da que foi usada no item 2.
funcao_format = ' {} mora no estado de/da/do {} '.format(nome, estado.upper())
print(funcao_format)