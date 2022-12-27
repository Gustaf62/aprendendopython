jogos = ['Hades', 'Celeste', 'Forza', 'Halo']

for jogo in jogos: #para cada jogo, dentro da lista de jogos, imprima jogo
    print(jogo)

for numero in range(0, 20, 2):   # para cada numero em um alcançe de 0 a 20 de 2 em 2, imprima esses numeros.
    print(numero)

nome = 'Gustavo Freitas'
for letra in nome:
    print(letra)

i = 0
while i < 10:                       #enquanto I for menor que 10, imprima isso:
    print('i ainda é menor que 10')
    i = i + 1                      #condição para i não ser menor que 10 para sempre
print('i é igual a 10: ', i)       #quando i não for mas menor que 10, imprima isso

numero = 0

while True:                #enquanto for verdade que (loop infinito)
    print(numero)
    if numero == 20:       #se o numero for igual a 20
        break              #pare o comando
    numero += 1            #o numero passa a somar de 1 em 1 de 0 até 20


