from time import sleep
sal = float(input('Qual seu salário? R$'))
print('\033[33mCalculando seu aumento...\033[m')
sleep(1)
if sal > 1250.00:
    sal = sal + (10/100*sal)
    print('Seu salário subiu para: \033[1;32;40mR${:.2f}\033[m'.format(sal))
else:
    sal = sal + (15/100*sal)
    print('Seu salário subiu para: \033[1;34;40mR${:.2f}\033[m'.format(sal))


