print('Vamos descobrir quanto de tinta será necessário para pintar está parede?(considere 1L de tinta = 2m²)')
larg=int(input('Qual a largura dessa parede?'))
alt=int(input('Qual a altura dessa parede?'))
area=larg*alt
print('A área dessa parede é de {}'.format(area))
tinta=area/2
print('Para pintar uma parede de {}m² será necessário {}L de tinta.'.format(area, tinta))
