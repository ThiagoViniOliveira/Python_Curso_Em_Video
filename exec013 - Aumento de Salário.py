salarioatual = float(input('Digite o seu salário atual: R$'))
aumento = salarioatual * 15 / 100
novosalario = salarioatual + aumento
print('Você recebia R${}, porém com aumento de 15%, você passa a receber R${}'.format(salarioatual, novosalario))