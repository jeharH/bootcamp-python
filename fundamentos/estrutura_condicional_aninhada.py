conta_normal = False
conta_universitaria = False
saldo = 2000
saque = 1500
cheque_especial = 450
conta_especial = True

if conta_normal:
    if saldo >= saque:
        print('Saque realizado com sucesso!')
    elif(saque <= (saldo + cheque_especial)):
        print('Saque realizado com o uso do cheque especial!')
    else:
        print('Não foi possível realizar o saque!')
if conta_universitaria:
    if saldo >= saque:
        print('Saque realizado com sucesso!')
    else:
        print('Saldo insuficiente!')
elif (conta_especial):
    print('Conta especial selecionada!')
else:
    print('Sistema não reconheceu o tipo de conta. Por favor, entre em contato com seu gerente.')