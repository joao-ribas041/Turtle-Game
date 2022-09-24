from turtle import Turtle

t = Turtle()
t.speed(1)
t.shape('turtle')


def acao_girar(turtle):
    acao = input('\nRotacionar para a direita[d] ou esquerda[e]? ')
    return acao


while True:
    while True:
        acao = input('\nRotacionar para a direita[d] ou esquerda[e]? ')
        if acao in 'DdEe':
            break
        else:
            continue

    if acao in 'Dd':
        rotacao = int(input('Quanto devemos rotacionar? '))
        t.right(rotacao)
    if acao in 'Ee':
        rotacao = int(input('Quanto devemos rotacionar? '))
        t.left(rotacao)

    while True:
        acao = input('\nDeseja ir para frete[f] ou para traz[t]? ')
        if acao in 'FfTt':
            break
        else:
            continue

    if acao in 'Ff':
        mov = int(input('Quantos pixels devemos percorrer? '))
        t.forward(mov)
    if acao in 'Tt':
        mov = int(input('Quantos pixels devemos percorrer? '))
        t.backward(mov)

    acao = input('\nDeseja continuar? [n] para encerrar: ')
    if acao == 'n':
        break
    else:
        continue
print('finalizado.')
