print('Convidados para o aniversário')
print('----------------------------------------------------')

numero_de_convidados = input('Digite o número de convidados: ')
lista_de_convidados = []

i = 1
while i <= int(numero_de_convidados):
    nome_do_convidado = input('Coloque o nome do convidado #' + str(i) + ': ')
    lista_de_convidados.append(nome_do_convidado)
    i += 1
print('## LISTA DE CONVIDADOS ##')
for convidado in lista_de_convidados:
    print(convidado)