# DESAFIO 1 ---------------------------------------------------

idades = {'joao': 20, 'bernardo': 12,'jehar': 25}

for nome in idades: # cada chave dentro da variável idades irá para a váriavel nome
    print(idades[nome]) # entre conchetes  ele mostrará o valor correspondente a cada chave

# DESAFIO 2 ---------------------------------------------------

numero = 1500

print(f'O número formatado para moeda seria: R${numero:,.2f}') # para formatar um numero dentro do Python é usado esse código

# DESAFIO 3 ---------------------------------------------------

vendas = 5000

if vendas > 1000:
    print('Você bateu a primeira meta')
while vendas > 3000:
    print('Você bateu a segunda meta!')
    break
while vendas > 4500:
    print('Você bateu a terceira meta!')
    break

# DESAFIO 4 ---------------------------------------------------

lista = ['carro', 'onibus', 'van', 'bicicleta']
#lista.append('moto')
#nova_lista = lista
nova_lista = lista.append('moto') # a função (ou método) 'append' adiciona um item no final da lista
print(lista)
print(nova_lista)