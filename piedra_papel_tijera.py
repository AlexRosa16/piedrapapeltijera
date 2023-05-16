import random

Piedra = 'piedra'
Papel = 'papel'
Tijera = 'tijera'
Opciones = [Piedra, Papel, Tijera]
OpcionesGanadoras = [[Papel, Piedra], [Tijera, Papel], [Piedra, Tijera]]
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


print("JUEGO : Piedra, papel y tijera")
while 1:
    SeguirJugando = input("Quieres jugar? (s/n): ")
    if 's' in SeguirJugando.lower():
        MovimientoGeneradoRandom = GeneradorOpcionRandom()
        while True:
            SeleccionarMovimiento = input(
                "Selecciona un movimiento ('p' para piedra / 'a' para papel / 't' para tijeras): ").lower()
            print(f"Elección del ordenador: {MovimientoGeneradoRandom}")
            if 'p' in SeleccionarMovimiento or 'a' in SeleccionarMovimiento \
                    or 't' in SeleccionarMovimiento or 'p' in SeleccionarMovimiento or\
                    'a' in SeleccionarMovimiento or 't' in SeleccionarMovimiento:
                if 'p' in SeleccionarMovimiento:
                    MovimientoUsuario = Piedra
                elif 'a' in SeleccionarMovimiento:
                    MovimientoUsuario = Papel
                elif 't' in SeleccionarMovimiento:
                    MovimientoUsuario = Tijera
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
