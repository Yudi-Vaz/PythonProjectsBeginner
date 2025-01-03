import random
from time import sleep
num = random.randint(1, 5)
print('-=-' * 20)
print('Pensei em um número entre 1 e 5.')
print('-=-' * 20)
resp = int(input(('Tente adivinhar qual esse número:')))
print('PROCESSANDO...')
sleep(2)
if num ==resp:
    print('Parabéns, você acertou!')
else:
    print('não, você errou, eu pensei em {}'.format(num))
