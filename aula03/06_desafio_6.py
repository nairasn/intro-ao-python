# # Você é a professora de Ciências e está lançando as notas das alunas.
# # Você quer criar um sistema no qual suas alunas podem ver suas notas digitando o nome.
# # As listas de alunas e notas se encontra abaixo. As notas podem variar de 0 a 100.
# # Nessas listas, as notas estão na mesma ordem dos nomes, ou seja, a aluna no índice 4 tirou a nota no índice 4.
import colorama
from colorama import Fore, Style
colorama.init()

alunas = ['Adriana', 'Bárbara', 'Franciele', 'Laís', 'Maria', 'Nayara', 'Patrícia', 'Renata', 'Sarah', 'Thainá']
notas = [78, 57, 80, 98, 54, 89, 90, 100, 71, 85]

# # # Comece o programa perguntando o nome da aluna.
nome_aluna = input('Digite seu nome para iniciar pesquisa de notas: ')
print(f'Nome buscado: {nome_aluna}')

# # # Procure o nome digitado na lista de nomes e imprima uma mensagem com a nota que ela tirou.
# # # Notas abaixo de 60 devem ser impressas com a cor vermelha, e notas a partir de 90 devem ser
# # # impressas com a cor verde.
# # # Se o nome digitado não existir na lista, imprima uma mensagem de erro usando a cor vermelha.

if nome_aluna in alunas:
    for i, aluna in enumerate (alunas):
        if aluna == nome_aluna:
            if notas[i] < 60:
                print('REPROVADA! A aluna ' + nome_aluna + ' tirou nota ' + colorama.Fore.RED + str(notas[i]) + colorama.Style.RESET_ALL+ ' :(')
            elif notas[i] > 60 and notas[i] < 90:
                print('APROVADA! A aluna ' + nome_aluna + ' tirou nota ' + colorama.Fore.YELLOW + str(notas[i]) + colorama.Style.RESET_ALL+ ' :)')
            elif notas[i] >= 90:
                print('APROVADA! A aluna ' + nome_aluna + ' tirou nota ' + colorama.Fore.GREEN + str(notas[i]) + colorama.Style.RESET_ALL + ' :)')
else:
    print(colorama.Fore.RED + 'ERRO!!! Nome não escontrado!')
