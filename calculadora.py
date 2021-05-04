titulo = 'Calculadora'
print(f'{titulo:=^40}')
print()
resp = 'S'
while resp == 'S':
    n1 = input('Primeiro Número: ').strip()
    while not n1.isnumeric():
        print('Valor inválido, você precisa digitar um número!')
        n1 = input('Digite novamente o primeiro número: ')

    n2 = input('Segundo Número: ').strip()
    while not n2.isnumeric():
        print('Valor inválido, você precisa digitar um número!')
        n2 = input('Digite novamente o segundo número: ')

    print('''Escolha um dos operadores abaixo:
    [ 1 ] Adição
    [ 2 ] Subtração
    [ 3 ] Multiplicação
    [ 4 ] Divisão''')
    op = input('Digite o número da operação desejada: ')
    while not op.isnumeric():
        op = input('Valor inválido! Digite novamente a operação desejada: ')

    op = int(op)
    n1 = int(n1)
    n2 = int(n2)
    while op < 1 or op > 4:
        op = int(input('Valor inválido! Digite novamente a operação desejada: '))

    if op == 1:
        print('{} + {} = {}'.format(n1, n2, n1 + n2))
    else:
        if op == 2:
            print('{} - {} = {}'.format(n1, n2, n1 - n2))
        else:
            if op == 3:
                print('{} x {} = {}'.format(n1, n2, n1 * n2))
            else:
                if op == 4:
                    print('{} x {} = {}'.format(n1, n2, n1 / n2))

    resp = str(input('Calcular novamente (S/N)? ')).upper().strip()
    while resp != 'S' and resp != 'N':
        print('Não entendi...')
        resp = str(input('Você quer calcular novamente (S/N)? ')).upper().strip()
print('Fim dos cálculos')

