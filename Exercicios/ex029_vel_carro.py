vel = float(input('Qual velocidade você estava dirigindo?'))
if vel > 80:
    print('Você ultrapassou o limite de velocidade, Você foi multado em R${:.2f}'.format((vel - 80) * 7  ))
else:
    print('Você está dentro do limite de velocidade. Tenha um bom dia!')
