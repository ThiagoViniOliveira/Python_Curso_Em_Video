largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))
metrosQuadrados = largura * altura
print('Ok, sua parede tem {} metros Quadrados'.format(metrosQuadrados))
tinta = 1
print('Para pintar sua parede você precisará de {} Litros de Tinta'.format(tinta * metrosQuadrados /2))