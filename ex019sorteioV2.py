import random
n1 = input ('Nome do 1° aluno:')
n2 = input ( 'Nome do 2° aluno:' )
n3 = input ( 'Nome do 3° aluno:' )
n4 = input ( 'Nome do 4° aluno:')
sort = random.choice ( [ n1, n2, n3 ,n4 ] )
print ( 'O aluno sorteado foi {}'.format(sort))

