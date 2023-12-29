""" /*
 * Crea una función que dibuje una escalera según su número de escalones.
 * - Si el número es positivo, será ascendente de izquiera a derecha.
 * - Si el número es negativo, será descendente de izquiera a derecha.
 * - Si el número es cero, se dibujarán dos guiones bajos (__).
 * 
 * Ejemplo: 4
 *         _
 *       _|       
 *     _|
 *   _|
 * _|
 * 
 */ """



def lader_print():
    steps: int = 0
    print('Dibujemos una escalera')
    steps = int(input('Ingrese el número de escalones: '))
    
    
    if steps == 0:
        print('__')
    elif steps > 0:
        print('  '*(steps+1)+'_')
        for step in range(steps,0,-1):
            space_blank = '  '*(step)
            print(f'{space_blank}_|')
    elif steps < 0:
        print(' _')
        for step in range(1,-steps,1):
            space_blank='  '*step
            print(f'{space_blank}|_')
            
            


if __name__ == '__main__':
    lader_print()
