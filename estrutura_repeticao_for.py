# texto = input('Informe um texto: ')
texto = ''
VOGAIS = 'AEIOU'


# exemplo utiliazando um iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print() # adiciona uma quebra de linha
    print('Executa')

# exemplo utiliazando a função built-in range
for numero in range(0, 102, 2):
    print(numero, end=' ')