frase = 'eu te amo'  #em uma string o python da a liberdade de fragmentar os caracteres
print(frase[0])      #o 0 representa o primeiro caractere da string
print(frase[1])      #o 1 representa o segundo, e assim por diante
print(frase[1:7])    # é possivel selecionar o a quantidade de elementos da str com o (:), espaços e caracteres são contabilizados
print(frase[0:9:2])  #é possivel realizar espaçamentos
print(frase[::-1])   #frase ao contrário com o espaçamento negativo

lista_filmes = ['toy story', 'moana', 'pinóquio', 'divertidamente'] #listas são definidas pelos colchetes e não são strings
lista_filmes.append('rei leão') #o .append adiciona elementos a lista, sempre na ultima posição
lista_filmes.remove('moana')  #.remove retira elementos da lista
lista_filmes.insert(1, 'cinderela') #o .insert escolhe a posição em que um elemento entrará na lista
lista_filmes[0] = 'toy story 2' #é possivel mudar de elemento com esse comando
print(lista_filmes)
print(lista_filmes[0])  # selecionar elementos de uma lista, começando por 0
print(lista_filmes[1:3])
print(lista_filmes[-1])  #com valores negativos é possivel começar a lista ou string de trás para frente
print(lista_filmes[-2])  # a contagem sempre começa como -1 sendo o ultimo elemento da lista/str

lista_nomes = ['maria', 'carlos', 'joão', 'vitória', 'maria']
contagem = lista_nomes.count('maria')       #.count conta o numero de elementos repetidos na lista
print(contagem)
print(len(lista_nomes))     #o len determina o numero de elementos de uma lista ou o de caracteres em uma string
lista_nomes.pop()    #o .pop retira o ultimo elemento da lista ou caractere da string
print(lista_nomes)

frase_2 = ('SUAVE, BROTHER?')
print(frase_2.lower())  #.lower transforma os caracteres em minusculos e .upper em maisuculo
frase_separada = frase_2.split(',') #o .split separa a string a partir do caractere escolhido nos parenteses e transforma em lista
print(frase_separada)
print(frase_separada[1])
frase_nova = frase_2 + ', vai fazer o que hoje?' #Concatenação de strings
print(frase_nova)
