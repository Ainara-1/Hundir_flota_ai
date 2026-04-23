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
        
    lista.append((fila,columna))
    return tablero, lista


# crear barcos aleatorios
#eslora=4
def barcos_rival(tablero):
    x=np.random.randint(9)
    print(x)
    y=np.random.randint(9)
    print(y)
    pos_inicial=(x,y)
    print(pos_inicial)
    orientacion = np.random.choice(["H","V"])
    print(orientacion)

    if orientacion == "V":
        if x+3<=9:
            tablero [x] [y]="O"
            x1=x+1
            tablero[x1] [y]="O"
            x2=x1+1
            tablero[x2] [y]="O"
            x3=x2+1
            tablero[x3] [y]="O" 
        else:
            print("Elija otra posicion")
        
    else:
        if y+3<=9:
            tablero[x][y]="O"
            y1=y+1
            tablero[x][y1]="O"
            y2=y1+1
            tablero[x][y2]="O"
            y3=y2+1
            tablero[x][y3]="O"
        else:
            print("Elija otra posicion")

    print(tablero)
    return(tablero)
                