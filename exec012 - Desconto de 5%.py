valor = float(input('Digite o valor do Produto: R$'))
desconto = valor * 5 / 100
novovalor = valor - desconto
print('O seu Produto custava R${}, porém com desconto de 5%, ficará R${}'.format(valor, novovalor))