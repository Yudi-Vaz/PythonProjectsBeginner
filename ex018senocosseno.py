import math
ang=float(input('Digite um ângulo:'))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))
print('O seno deste número é {:.2f}, o cosseno é {:.2f}, e a tangente é {:.2f}.'.format(sen, cos,tang ))
