n = int(input())

for _ in range(n):
    A, B = input().split()

    if A[-len(B):] == B:
        print('encaixa')
    else:
        print('nao encaixa')


#         ''' 
# IMPORTANTE: As funções "input" e "print" são acessíveis nativamente em Python, onde:  
#  - "input": função que permite a leitura de uma entrada do usuário. Lembre-se que, em alguns 
#    casos, é necessário converter/tratar os dados de entrada; 
#  - "print": função que imprime um texto enviado em seu parâmetro, a qual é essencial para a 
#    impressão dos dados de saída. 
# '''
# N = int(input())

# while(n > 0):
#     ''' 
#     TODO  Verifique, para cada entrada A e B, se os dois valores são compatíveis e imprima se
#     "encaixa" ou "não encaixa" para cada uma das relações N vezes.
#     '''