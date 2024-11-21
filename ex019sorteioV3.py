import random
sorteio=input('Digite qualquer coisa para sortear uma carta numerada de 1 á 10:')
carta=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
resultado=random.choice(carta)
print('A carta sorteada foi {}'.format(resultado))
