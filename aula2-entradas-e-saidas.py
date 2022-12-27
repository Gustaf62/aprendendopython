nome = input('Digite seu nome: ')                   #variáveis sempre são escritas com letras minusculas
cpf = input('Digite seu CPF:')                      #se possuirem mais de um nome devem ser espaçadas por (_)
endereço = input('Digite seu endereço: ')           #podem ser de vários tipos, string int e float
email = input('Informe seu email principal: ')      #para descobrir o tipo basta usar a função type
idade = input('Informe sua idade: ')
telefone = input('Informe seu número para contato: ')

print('Nome: ', nome)
print('CPF:: ', cpf)
print('Endereço: ', endereço)
print('email: ', email)
print('Idade: ', idade, 'anos')
print('contato: ', telefone)