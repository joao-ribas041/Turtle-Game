from turtle import Turtle

t = Turtle()
t.speed(1)
t.shape('turtle')

while True:
    acao = input('\nRotacionar para a direita[d] ou esquerda[e]? ')
    if acao == 'd':
        rotacao = int(input('Quanto devemos rotacionar? '))
        t.right(rotacao)
    elif acao == 'e':
        rotacao = int(input('Quanto devemos rotacionar? '))
        t.left(rotacao)

    acao = input('\nDeseja ir para frete[f] ou para traz[t]? ')
    if acao == 'f':
        mov = int(input('Quantos pixels devemos percorrer? '))
        t.forward(mov)
    elif acao == 't':
        mov = int(input('Quantos pixels devemos percorrer? '))
        t.backward(mov)

    acao = input('\nDeseja continuar? [n] para encerrar: ')
    if acao == 'n':
        break
    else:
        continue

print('finalizado.')
