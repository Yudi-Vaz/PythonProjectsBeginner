preco=float(input('Qual o preço do produto? R$'))
parcelado = float ( preco / 4 )
valorfinal=float(preco+(preco*15/100))
valoravista=float(preco-(preco*30/100))
print('Você pode parcelar seu produto em até 4 parcelas de R${:.2f} e um juros de 15%,\ncom o valor final de R${:.2f}.\nOu você pode pagar a vista com um desconto de 30%, que resultaria no valor de R${:.2f}'.format(parcelado, valorfinal, valoravista))