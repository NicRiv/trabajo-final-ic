"""
Trabajo Final - IC.
https://github.com/NicRiv/trabajo-final-ic

UNRN
Rivera, Nicolás.
"""

# Función principal
def main():
    # Inicializa variable de recuento de piezas
    total_de_piezas = 0
    
    while True: # primer ciclo
        ### Sección Pieza ###
        print('Ingrese el código de la pieza.')
        codigo_de_pieza = input('> ') # se asigna la entrada a la variable CP.
        if not codigo_valido(codigo_de_pieza):
            # Error: la entrada ingresada no es valida
            print('Código no valido.')
    
        else:
            # La entrada es valida, se procesa el valor como tipo entero.
            codigo_de_pieza = int(codigo_de_pieza)
            
            if codigo_de_pieza != 0:
                # Inicializa variable del precio de la pieza
                precio_de_la_pieza = 0
                # Muestra por pantalla el valor del codigo de la pieza
                print(f'el codigo es: {codigo_de_pieza}')
                
                while True: # segundo ciclo
                    ### Sección Componente ###
                    print('Ingrese el código del componente.')
                    codigo_de_componente = input('> ') # Se asigna el valor de entrada a la variable CC.
                    
                    if not componente_valido(codigo_de_componente, codigo_de_pieza):
                        # Error: la entrada ingresada no es valida
                        print('Componente no valido')
                        
                    else:
                        # La entrada es valida, se procesa como tipo entero
                        codigo_de_componente = int(codigo_de_componente)
                        
                        if codigo_de_componente != 0:
                            print(f'El código del componente es: {codigo_de_componente}')
                            
                            # Sección precio del componente
                            print('Ingrese el precio del componente.')
                            precio_del_componente = input('> ')
                            
                            if not precio_valido(precio_del_componente):
                                print('Precio no valido.')
                            else:
                                precio_del_componente = float(precio_del_componente)
                                precio_de_la_pieza += precio_del_componente
                            
                        else:
                            # La entrada es 0, finaliza el recuento de componentes
                            total_de_piezas += 1 # Agrega nueva pieza
                            print(f'El precio de la piezas es: {precio_de_la_pieza}')
                            break

            # finaliza programa al ingresar 0 como valor de entrada
            else:
                print(f'El total de las piezas procesadas es de: {total_de_piezas}')
                break


# Subprocesos
def codigo_valido(codigo, componente = False):
    if codigo.isnumeric():
        # Se valida el código de pieza
        if not componente:
            if int(codigo) >= 0 and int(codigo) <= 99:
                return True
        # Se valida el código de componente
        else:
            if int(codigo) >= 1 and int(codigo) <= 9999:
                return True
    # No pasa los requisitos de validación.
    return False

def componente_valido(codigo, pieza):
    if codigo_valido(codigo, True):
        if int(codigo) % pow(10, len(str(pieza))) == pieza:
            # El código del componente corresponde a la pieza
            return True
    # No pasa los requisitos de validación.
    return False
        

def precio_valido(precio):
    try:
        float(precio)
        if float(precio) >= 10 and float(precio) <= 999.99:
            # La entrada es de tipo flotante y se encuentra entre el rango.
            return True
        
        # No pasa los requisitos de validación.
        else:
            return False
        
    # No pasa los requisitos de validación.    
    except ValueError:
        return False

if __name__ == '__main__':
    main()