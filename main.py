
from utils import crear_tablero, colocar_barcos, disparar

import time
import numpy as np

tablero_jugador_disparos = crear_tablero()
tablero_jugador_barcos = crear_tablero()


tablero_rival_disparos = crear_tablero()
tablero_rival_barcos = crear_tablero()

#lista barcos jugador real
#li_bar_jug_real= [[(0,1),(0,2)],[(2,3),(2,4)],[(4,1),(4,2)],[(6,3),(7,3),(8,3)],[(4,5),(5,5),(6,5)],[(3,8),(4,8),(5,8),(6,8)]]
#tablero_jugador_barcos_real = colocar_barcos(li_bar_jug_real,tablero_jugador_barcos)
#print(tablero_jugador_barcos_real)
#print("-------------")


#lista barcos rival real
#li_bar_riv_real= [[(2,2),(2,3)],[(5,0),(5,1)],[(9,1),(9,2)],[(3,5),(3,6),(3,7)],[(9,2),(9,3),(9,4)],[(8,5),(8,6),(8,7),(8,8)]]
#tablero_rival_barcos_real = colocar_barcos(li_bar_riv_real,tablero_rival_barcos)
#print(tablero_rival_barcos_real)
#print("----------------")

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
        print("TABLERO RIVAL BARCOS-55")
        print(tablero_rival_barcos)
    #print("TABLERO JUGADOR BARCOS-57")
    #print(tablero_jugador_barcos)
    else:
        print("FIN DEL JUEGO")




