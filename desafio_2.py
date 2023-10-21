mes = int(input())

meses = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}

if mes in meses:
    print(meses[mes])
else:
    print('Insira ummês válido!')


# while  True:
#     mes = int(input())

    

#     if mes == 1:
#         print('January')

#     elif mes == 2:
#         print('February')

#     elif mes == 3:
#         print('March')

#     elif mes == 4:
#         print('April')

#     elif mes == 5:
#         print('May')

#     elif mes == 6:
#         print('June')

#     elif mes == 7:
#         print('July')

#     elif mes == 8:
#         print('August')

#     elif mes == 9:
#         print('September')

#     elif mes == 10:
#         print('October')

#     elif mes == 11:
#         print('November')

#     elif mes == 12:
#         print('December')



# ''' 
# IMPORTANTE: As funções "input" e "print" são acessíveis nativamente em Python, onde:  
#  - "input": função que permite a leitura de uma entrada do usuário. Lembre-se que, em alguns 
#    casos, é necessário converter/tratar os dados de entrada; 
#  - "print": função que imprime um texto enviado em seu parâmetro, a qual é essencial para a 
#    impressão dos dados de saída. 
# - "dict{}": dicionários possuem uma relação de chave - valor. Para cada chave haverá um valor.
# '''
# month = input()

# months_dict = {
#     ''' 
#     TODO Faça uma relação entre as possíveis entradas e os meses (em inglês).
#     TODO Imprima o valor de cada chave em relação as entradas do programa.
#     '''
# }