# T = input('Digite seu tweet: ')

# tamanhoT = 0

# for caracter in T:
#     tamanhoT += 1

# if tamanhoT > 140:
#     print('MUTE')

# elif tamanhoT <= 140:
#     print('TWEET')

T= input()

if len(T) > 140:
    print('MUTE')

else:
    print('TWEET')

# o comando len() verifica o cumprimento do texto ou da string








#     ''' 
# IMPORTANTE: As funções "input" e "print" são acessíveis nativamente em Python, onde:  
#  - "input": função que permite a leitura de uma entrada do usuário. Lembre-se que, em alguns 
#    casos, é necessário converter/tratar os dados de entrada; 
#  - "print": função que imprime um texto enviado em seu parâmetro, a qual é essencial para a 
#    impressão dos dados de saída. 
# '''
# # T = input()
#     ''' 
#     TODO Ler a variável de entrada e verificar se ela possui mais ou menos que 140 caracteres.
#     Se for maior imprima "MUTE" e se for igual ou menor imprima "TWEET".
#     '''
    