import random
n1 = str(input('Digite o nome do 1° aluno:'))
n2 = str(input('Digite o nome do 2° aluno:'))
n3 = str(input('Digite o nome do 3° aluno:'))
lista = ([n1, n2, n3])
random.shuffle(lista)
print('A ordem desses alunos será:{}'.format(lista))

