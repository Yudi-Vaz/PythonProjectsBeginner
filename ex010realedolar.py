print('Seja bem-vindo ao convertor de moedas.')
nome=str(input('Qual seu nome?'))
reais=float(input('Qual seu valor em reais?(considere US$1,00 = R$5,79)'))
dolar=reais*5.79
print('{}, o valor de R${:.2f} em dólares é US${}'.format(nome, reais, dolar))
