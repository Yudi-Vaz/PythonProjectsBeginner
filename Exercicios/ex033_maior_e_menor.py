from time import sleep
num1 = int(input('Digite um número:'))
num2 = int(input('Digite outro número:'))
num3 = int(input('Digite mais um  número:'))
print('PROCESSANDO...')
sleep(2)
if num1 > num2 > num3:
    print('{} é o maior número, e {} é o menor número'.format(num1, num3))
else:
    b = [num1, num2, num3]
    b.sort(reverse=True) #Diz qual número dentro de uma lista é o maior
    print('{} é o maior número, e {} é o menor número'.format( b[0], b[-1] )) #lista utilizada no "b (b é uma variável) .sort"
