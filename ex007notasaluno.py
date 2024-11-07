print('OLá estudante, seja bem-vindo!')
nome=str(input('Qual seu nome?'))
print('Muito prazer {}! Para descobrir sua média de notas, digite suas notas de língua Portuguesa e Matemática no campo abaixo:'.format(nome))
lp=int(input('Nota de língua portuguesa:'))
mt=int(input('Nota de Matemática:'))
r=lp+mt
print('{}, a sua média de notas é {}.'.format(nome, r/2 ))
