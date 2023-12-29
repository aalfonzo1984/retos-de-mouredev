""" /*
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 * 
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.   
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
 */ """
 
 
scale_point: list[str] = ['15', '30', '45']

count: dict[int] = {'P1': 0,
                    'P2': 0}


def play(secuence):
    playing: dict = {
        'P1': {'point': 'Love'},
        'P2': {'point': 'Love'}
    }

    for player in secuence:

        if playing['P1']['point'] == '45' and playing['P2']['point'] == '45':
            playing[player]['point'] = 'Ventaja'
            print(f'Ventaja {player}')
        elif playing['P1']['point'] == 'Ventaja' or playing['P2']['point'] == 'Ventaja':
            if playing[player]['point'] == 'Ventaja':
                return player
            else:
                playing['P1']['point'] = '45'
                playing['P2']['point'] = '45'
                print('Deuce')
        else:
            playing[player]['point'] = scale_point[count[player]]
            if playing['P1']['point'] == '45' and playing['P2']['point'] == '45':
                print('Deuce')
            else:
                print(f"{playing['P1']['point']} - {playing['P2']['point']}")
            count[player] += 1

    return (player)


if __name__ == '__main__':

    secuence: list[str] = ['P1', 'P1', 'P2', 'P2',
                           'P1', 'P2', 'P1', 'P2', 'P1', 'P2', 'P2']

    win = play(secuence)
    print(f'Ha ganado el jugador {win}')