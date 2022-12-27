idade = int(input('Escreva sua idade:'))     #condcionais: if, else e elif
peso = float(input('Informe seu peso: '))    #elif serve para evitar a repetição de vários if e else
altura = float(input('Informe sua altura: ')) #os condicionais devem ser identados,com dois pontos e tab sempre

if altura >= 1.70 and peso >= 60.0 and idade >= 18: #se os valores de altura,peso e idade estiverem de acordo, imprima isso
    print("Você está apto para servir")
else:                                             #caso não estiverem de acordo, imprima isso
    print('Você não está apto a servir')