
from utils import crear_tablero, colocar_barcos, disparar

import time
import numpy as np

tablero_jugador_disparos = crear_tablero()
tablero_jugador_barcos = crear_tablero()


tablero_rival_disparos = crear_tablero()
tablero_rival_barcos = crear_tablero()

#introducimos los barcos jugador demo
li_bar_jug = [[(0,1),(0,2)],[(7,8),(8,8)]]

#introducimos los barcos del rival demo
li_bar_riv = [[(9,1),(9,2)],[(7,2),(7,1)]]

tablero_jugador_barcos = colocar_barcos(li_bar_jug,tablero_jugador_barcos)
tablero_rival_barcos = colocar_barcos(li_bar_riv,tablero_rival_barcos)

print("      TABLERO RIVAL BARCOS      ")
print(tablero_rival_barcos)
print("          TABLERO JUGADOR BARCOS      ")
print(tablero_jugador_barcos)
time.sleep(3)
print("Tu turno jugador") 

lis_disp_jug=[]
lis_disp_riv= []

while True:
    pos_o = np.any(tablero_rival_barcos=="O")
    if pos_o == True:
        tablero_rival_barcos,lis_disp_jug= disparar(tablero_rival_barcos,lis_disp_jug)
        time.sleep(3)
        print("TABLERO RIVAL BARCOS")
        print(tablero_rival_barcos)
    
    else:
        print("FIN DEL JUEGO")




