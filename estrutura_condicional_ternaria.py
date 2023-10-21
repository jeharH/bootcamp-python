saldo = 2000
saque = 2495

status = 'Sucesso' if saldo >= saque else 'Falha'

print(f'{status} ao realizar o saque!')