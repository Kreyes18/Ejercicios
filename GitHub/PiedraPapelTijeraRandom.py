import random
a='si'
while a == 'si':
    modo=input('Que modo desea jugar 1 o 2.\n1.Multijugador\n2.PlayervsComputer\n')
    if modo == '1':
        opciones=['tijera','papel','piedra']
        usuario1=input('Elige:').lower()
        
        opciones=['tijera','papel','piedra']
        usuario2=input('Elige:').lower()
        if usuario1 not in opciones:
            print('Error')
            quit()
        if usuario2 not in opciones:
            print('Error')
            quit()
        if usuario1 == usuario2:
            print('Empate')
        elif usuario1 == 'tijera' and usuario2 == 'piedra' or usuario1 == 'piedra' and usuario2 == 'papel' or usuario1 == 'papel' and usuario2 == 'tijera':
            print('Has ganado jugador 2!')
        else:
            print('Haz ganado jugador 1!')
    elif modo == '2':
        opciones=['tijera','papel','piedra']
        usuario=input('Elige:').lower()
        ordenador=random.choice(opciones)
        if usuario not in opciones:
            print('Error')
            quit()
        if usuario == ordenador:
            print('Empate')
        elif usuario == 'tijera' and ordenador == 'piedra' or usuario == 'piedra' and ordenador == 'papel' or usuario == 'papel' and ordenador == 'tijera':
            print('Has perdido!')
        else:
            print('Haz ganado!')
    else:
        print('El numero digitado no concuerda, Saliendo del programa...')
        break
    a=input('Desea seguir jugando\n').lower()

