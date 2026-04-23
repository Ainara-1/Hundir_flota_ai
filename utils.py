import numpy as np

def crear_tablero():
    tablero = np.full((10,10),"-")
    return tablero

def colocar_barcos(lista_barcos, tablero):
    for i in lista_barcos:
        for j in i:
            tablero[j]="O"
    return tablero
    
def disparar(tablero, lista):
    fila=int(input("fila:"))
    columna=int(input("Columna:"))

    if tablero[fila][columna] == "O":
        tablero[fila][columna] ="X"
        print ("TOCADOOO!!!")
    else:
        tablero[fila][columna] = "#"
        print("AGUAAA!!!")
        #turno = False
    lista.append((fila,columna))
    return tablero, lista


