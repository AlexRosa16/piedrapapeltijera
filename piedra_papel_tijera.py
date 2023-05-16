import random

Piedra = 'piedra'
Papel = 'papel'
Tijera = 'tijera'
Lagarto = 'lagarto'
Opciones = [Piedra, Papel, Tijera, Lagarto]
OpcionesGanadoras = [[Papel, Piedra], [Tijera, Papel], [Piedra, Tijera], [Lagarto, Papel], [Piedra, Lagarto],
                     [Tijera, Lagarto]]
OpcionesPerdedoras = [[Piedra, Papel], [Papel, Tijera], [Tijera, Piedra]]
MovimientoUsuario = ""


def GeneradorOpcionRandom():
    MovimientoRandom = random.choice(Opciones)
    return MovimientoRandom


def VerificarJugada(MovimientoUsuariio, MovimientoCompu):
    if [MovimientoUsuariio, MovimientoCompu] in OpcionesGanadoras:
        return 1
    elif [MovimientoUsuariio, MovimientoCompu] in OpcionesPerdedoras:
        return -1
    return 0


print("JUEGO : Piedra, papel, tijera y lagarto")
while 1:
    SeguirJugando = input("Quieres jugar? (s/n): ")
    if 'terminar' in SeguirJugando.lower():
        print("Tienes miedo?")
        SeguirJugando = input("Quieres jugar esta vez no te cagues? (s/n): ")
    if 's' in SeguirJugando.lower():
        MovimientoGeneradoRandom = GeneradorOpcionRandom()
        while True:
            SeleccionarMovimiento = input(
                "Selecciona un movimiento ('p' para piedra / 'a' para papel / 't' para tijeras / \
                'l' para lagarto): ").lower()
            print(f"Elección del ordenador: {MovimientoGeneradoRandom}")
            if 'p' in SeleccionarMovimiento or 'a' in SeleccionarMovimiento \
                    or 't' in SeleccionarMovimiento or 'p' in SeleccionarMovimiento or \
                    'a' in SeleccionarMovimiento or 't' in SeleccionarMovimiento or 'l' in SeleccionarMovimiento:
                if 'p' in SeleccionarMovimiento:
                    MovimientoUsuario = Piedra
                elif 'a' in SeleccionarMovimiento:
                    MovimientoUsuario = Papel
                elif 't' in SeleccionarMovimiento:
                    MovimientoUsuario = Tijera
                elif 'l' in SeleccionarMovimiento:
                    MovimientoUsuario = Lagarto
                print(f"Elección del usuario: {MovimientoUsuario}")
                if VerificarJugada(MovimientoUsuario, MovimientoGeneradoRandom) == 1:
                    print("Gana el usuario !!!")
                elif VerificarJugada(MovimientoUsuario, MovimientoGeneradoRandom) == -1:
                    print("Gana el ordenador !!!")
                elif VerificarJugada(MovimientoUsuario, MovimientoGeneradoRandom) == 0:
                    print("Empate !!!")
                elif VerificarJugada(MovimientoUsuario, MovimientoGeneradoRandom) == 2:
                    print("Ganan ambos !!!")
                elif VerificarJugada(MovimientoUsuario, MovimientoGeneradoRandom) == 3:
                    print("Pierden ambos !!!")
                break
            else:
                print("Entrada incorrecta. Vuelve a intentar.")
    elif 'n' in SeguirJugando.lower():
        break
    else:
        print('Entrada incorrecta. Vuelve a intentar.')
    print()
