menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair


==>'''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == 'd':
        valor = float(input('Informe o valor de depósito: '))
        if valor <= 0:
            valor = 0
            print('Depósito inválido!')
        elif valor > 0:
            saldo = saldo + valor
            extrato = extrato + f'Depósito de R${valor:,.2f} reais.\n'
        print(f'Deposito de R${valor:,.2f} reais realizado com sucesso.')

    elif opcao == 's':
        saque = float(input('Informe o valor de saque: '))
        if saque > limite:
            print('Seu limite de saque diário não pode passar 500 reais!')
        elif saldo <= 0:
            print('Operação inválida!')
        elif saque > saldo:
            print('Saldo insuficiente para realizar esse saque, tente novamente com um valor menor.')
        elif numero_saques >= LIMITE_SAQUES:
            print('Operação falhou! Número de saques diários excedido.')
        elif saque <= saldo:
            saldo = saldo - saque
            numero_saques = numero_saques + 1
            extrato = extrato + f'Saque de R${saque:,.2f}\n'
            print(f'Saque de R${saque:,.2f} reais realizado com sucesso. Saldo: R${saldo:,.2f}')
        

    elif opcao == 'e':
        if not extrato:
            print('Não houve movimentações.')
            print(f'Seu atual saldo é de R${saldo:,.2f}')
        else:
            print(f' EXTRATO '.center(51, '#'))
            print(extrato + f'\nSeu atual saldo é de R${saldo:,.2f}')
            print('###################################################')

    elif opcao == 'q':
        break

    else:
        print('Operação inválida, por favor selecione novamente a operação desejada!')
