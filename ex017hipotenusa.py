import math
cat1=float(input('Digite o valor de um cateto oposto de um triângulo:'))
cat2=float(input('Digite o valor do cateto adjascente desse triângulo:'))
print('A hipotenusa deste triângulo é {:.2f}.'.format(math.hypot(cat1, cat2)))

