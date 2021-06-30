print('---------- Vamos verificar se você PODE ou NÃO pegar um emprestimo... ----------')

nome = str(input('Qual o seu nome? '))
idade = int(input('Qual a sua idade? '))

menor = 18

def verificar_emprestimo():
    if idade >= menor:
        print(f'{nome}, você pode pegar o emprestimo.')
        print('========== Vamos calcular o seu empréstimo. ==========')
        def valor_emprestimo():
            valor = float(input('Qual o valor do seu empréstimo? '))
            print('========================================================')
            print('A cada parcela é acrescentado 4% no valor do empréstimo...')
            print('========================================================')
            parcela = int(input('Quantas parcelas você quer dividir? '))
            valor_total = (valor / parcela) 
            juros_parcela = (4 / 100) * valor_total
            valor_parcela = valor_total + juros_parcela
            emprestimo_total = valor_parcela * parcela
            print('========================================================')
            print(f'{nome}, suas parcelas serão de R$ {valor_parcela:.2f}.')
            print('*********************************************************')
            print(f'O valor total do seu emprestimo será R$ {emprestimo_total:.2f}.')
        valor_emprestimo()
    else:
        print(f'{nome}, você é menor de 18 anos e NÃO pode pegar o emprestimo.')

verificar_emprestimo()
