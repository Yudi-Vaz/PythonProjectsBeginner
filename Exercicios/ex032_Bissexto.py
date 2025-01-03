from datetime import date
ano = int(input('Digite um ano qualquer para analisarmos ( Digite 0 para analisar o ano atual ):'))
if ano == 0:
    date.today().year #pega o ano da data atual
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: #calcula se o ano é bissexto
    print('Esse ano é (ou foi) Bissexto pois tinha/tem 366 dias')
else:
    print('Esse ano não era/é Bissexto pois tem/tinha 365 dias')
