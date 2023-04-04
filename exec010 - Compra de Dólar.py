carteira = float(input('Quanto você tem na carteira? '))
dolar = 5.17
cambio = carteira / dolar
if carteira == 5.17:
    print('Com R$ {} reais, você pode comprar $ {} dólar.'.format(carteira, cambio))
if carteira >= 10.34:
    print('Com R$ {} Reais, você pode comprar $ {} Dólares.'.format(carteira, cambio))



