from turtle import Turtle

t = Turtle()
t.speed(1)
t.shape('turtle')


def acao_girar(turtle):
    acao = input('\nRotacionar para a direita[d] ou esquerda[e]? ')
    if acao in 'Dd':
        rotacionar_direita(turtle)
        return True
    elif acao in 'Ee':
        rotacionar_esquerda(turtle)
        return True
    else:
        return False


def rotacionar_direita(turtle):
    rotacao = int(input('Quanto devemos rotacionar? '))
    t.right(rotacao)


def rotacionar_esquerda(turtle):
    rotacao = int(input('Quanto devemos rotacionar? '))
    t.left(rotacao)


while True:
    while True:
        if acao_girar(t) == False:
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
