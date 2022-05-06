from datetime import datetime, timedelta

# Peça para o usuário digitar a data de seu próximo aniversário no formato brasileiro
aniversario = input('Digite a data do seu próximo aniversário no formato brasileiro (dd/mm/aaaa): ')
data = datetime.strptime(aniversario, '%d/%m/%Y')
proximo_niver = data - datetime.now()

# Imprima uma mensagem dizendo quantos dias faltam para o aniversário dele
print(f'Faltam {proximo_niver.days} dias para o seu aniversário!! ')

# Pergunte ao usuário se ele(a) gosta de aniversário e salve a resposta
gosta_de_aniversario = input('Você gosta de fazer aniversário? (responda com sim/nao): ')

# Pergunte ao usuário se ele(a) vai fazer festa e salve a resposta
fazer_festa = input('Você irá fazer festa? (responda com sim/nao): ')

# Imprima uma mensagem dizendo se o usuário vai ganhar presente ou não
# A regra é: o usuário só pode ganhar presente se gostar de aniversário e for fazer festa.

if gosta_de_aniversario == 'sim' and fazer_festa == 'sim':
    print(' Surpresa!!! Você ganhará presente!!! *-* ')
else:
    print('Que pena.. Não tem presente esse ano...')