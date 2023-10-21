MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input('Informe sua idade: '))

if idade >= MAIOR_IDADE:
    print('Maior de idade! Pode tirar a CNH!')

if idade < MAIOR_IDADE:
    print('Você ainda não pode tirar a CNH!')


if idade >= MAIOR_IDADE:
    print('Maior de idade! Pode tirar a CNH!')
else:
    print('Você ainda não pode tirar a CNH!')


if idade >= MAIOR_IDADE:
    print('Maior de idade! Pode tirar a CNH!')
elif idade == IDADE_ESPECIAL:
    print('Pode fazer aulas práticas e não as teóricas.')
else:
    print('Você ainda não pode tirar a CNH!')