from turtle import Turtle

t = Turtle()
t.speed(1)
t.shape('turtle')


def acao_girar(turtle):
    while True:
        acao = input('\nRotacionar para a direita[d] ou esquerda[e]? ')
        if acao in 'DdEe':
            break

    if acao in 'Dd':
        rotacionar_direita(turtle)
    elif acao in 'Ee':
        rotacionar_esquerda(turtle)

def acao_andar(turtle):
    while True:
        acao = input('\nDeseja ir para frete[f] ou para traz[t]? ')
        if acao in 'FfTt':
            break

    if acao in 'Ff':
        andar_frente(turtle)
    elif acao in 'Tt':
        andar_traz(turtle)

def acao_continuar():
    while True:
        acao = input('\nDeseja continuar? [n] para encerrar: ')
        if acao in 'Nn':
            break
        else:
            continue



def percorrer():
    mover = int(input('Quantos pixels devemos percorrer? '))
    return mover

def girar():
    rotacionar = int(input('Quanto devemos rotacionar? '))
    return rotacionar

def rotacionar_direita(turtle):
    rotacao = girar()
    t.right(rotacao)

def rotacionar_esquerda(turtle):
    rotacao = girar()
    t.left(rotacao)

def andar_frente(turtle):
    mover = percorrer()
    t.forward(mover)

def andar_traz(turtle):
    mover = percorrer()
    t.backward(mover)

while True:
    acao_girar(t)
    acao_andar(t)




    acao = input('\nDeseja continuar? [n] para encerrar: ')
    if acao == 'n':
        break
    else:
        continue
print('finalizado.')
