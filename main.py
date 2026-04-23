
from utils import crear_tablero, colocar_barcos, disparar

import time

tablero_jugador_disparos = crear_tablero()
tablero_jugador_barcos = crear_tablero()


tablero_rival_disparos = crear_tablero()
tablero_rival_barcos = crear_tablero()

#introducimos los barcos jugador
li_bar_jug=[[(0,1),(0,2)],[(7,8),(8,8)]]
#introducimos los barcos del rival
li_bar_riv=[[(9,1),(9,2)],[(7,2),(7,1)]]

tablero_jugador_barcos=colocar_barcos(li_bar_jug,tablero_jugador_barcos)
tablero_rival_barcos=colocar_barcos(li_bar_riv,tablero_rival_barcos)

print("      TABLERO RIVAL BARCOS      ")
print(tablero_rival_barcos)
print("          TABLERO JUGADOR BARCOS      ")
print(tablero_jugador_barcos)
time.sleep(3)
print("Tu turno jugador")




