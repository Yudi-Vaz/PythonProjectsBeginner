a = float(input('Digite o cumprimento da primeira reta: '))
b = float(input('Digite o cumprimento da segunda reta: '))
c = float(input('Digite o cumprimento da terceira reta:'))
if a < b + c and b < a + c and c < b + a:
    print('É possível formar um triãngulo!')
else:
    print('Não é possível formar um triângulo!')
