lista = ['halo' , 'gears']      #List []
tuplas = ('forza' , 'redfall')  #Tuple  () serve para garantir coisas que não devem ser alteradas
dicionário = {'halo' : 'FPS' , 'forza' : 'corrida'} #Dict - "{}" armazena informações, sendo a chave 'halo' e seu valor 'FPS'
conjunto = {'GOD' , 'days gone'}           #Set - itens iguais não são contabilizados, e não é ordenado
                                       # Listas, dicionários e conjuntos são dinamicos, apenas tuplas são imutáveis

print(tuplas[0]) 
for jogo in tuplas:
    print(jogo)                        #ambos comandos funcionam em listas tuplas e conjuntos, menos em dicionários
if 'halo' in lista:   
    print('halo está na lista')

print(dicionário['forza'])             #dicionários não possuem indices (0,1,2,3), a pesquisa se dá por meio das chaves
if 'FPS' in dicionário.values():       #se fps está entre os valores do meu dicionário, imprima isso:
    print('FPS é um valor')            #são um ótimo mecanismo de busca, melhor que as listas.

for chaves in dicionário.keys():
    print(chaves)

dicionário['forza'] = 'Forza horizon'  #mutabilidade do dicionário, mudança de valor da chave
dicionário['gears'] = 'tps'            #adição de novas chaves e valores
print(dicionário)

conjunto.add('Uncharted')              #por nãoo serem ordenados, conjuntos são muito mais efetivos para busca que listas
conjunto.add('GOD')                    #conjuntos não contabilizam elementos iguais
print(conjunto)

#######VAZIOS#######                   #É possivel colocar estruturas de dados dentro de outras
lista2 = [] 
tuplas2 = ()
dicionário2 = {}
conjunto2 = set()