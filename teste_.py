carros = ['gol', 'celta', 'palio']

for indice, carro in enumerate(carros):
    print(f'{indice}: {carro}')

teste = [n**2 if n > 6 else n for n in range(10) if n % 2 == 0]
print(teste)