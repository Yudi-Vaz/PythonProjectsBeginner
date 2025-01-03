distancia = float(input('Qual a distância da sua viagem?'))
preco20 = distancia * 0.50 #valor para viagens até 200km
preco21 = distancia * 0.45 #valor para viagens que tenham mais de 200km
if distancia < 201:
    print('Então valor da sua passagem é R${:.2f}'.format(preco20))
else:
    print("Então o valor da sua passagem é R${:.2f}".format(preco21))
