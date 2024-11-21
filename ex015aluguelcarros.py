dias=float(input('Durante quantos dias você alugou o carro?:'))
km=float(input('Quantos km foram rodados?:'))
valfinal=float((dias*60)+(km*0.15))
print('O valor á se pagar pelo aluguel do carro é R${:.2f}'.format(valfinal))
