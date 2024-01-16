##########################################
#                                        #
#  Programe sus funciones aquí           #
#                                        #
##########################################

def disparo(tablero, barcos, fila, columna):
    b=barcos
    t=tablero
    Paro=True
    for casilla in b:
        if casilla[1]==1 and Paro:
            if fila in range(casilla[2],casilla[2]+casilla[0]):
                if columna==casilla[3]:
                    tablero[fila][columna]="O"
                    Paro= False
                else:
                    tablero[fila][columna]=" "
                    
                    
            else:
                tablero[fila][columna]=" "
                    

        if casilla[1]==2 and Paro:
            if columna in range(casilla[3],casilla[0]+casilla[3]):
                if fila==casilla[2]:
                    tablero[fila][columna]="O"
                    Paro = False
                else:
                    tablero[fila][columna]=" "
            else:
                tablero[fila][columna]=" "
                    

                    
            

   


def destruidos(tablero, barcos):
    Paro= True
    cant_disparos=0
    barcos_dest=0
    for casilla in barcos:
        if casilla[1]==1 and Paro:
            for j in range(barcos[2],barcos[2]+barcos[0]):
                if tablero[j][barcos[3]]=="O" and tablero[j][barcos[3]]==" " and tablero[j][barcos[3]]=="-":
                    tablero[j][3]=="X"
                    cant_disparos+=1
                if cant_disparos==barcos[0]:
                    barcos_dest+=1
                    
                    
        if casilla[1]==2 and Paro:
            for j in range(casilla[3],casilla[3]+casilla[0]):
                if tablero[barcos[2]][j]=="O" and tablero[barcos[2]][j]==" " and tablero[barcos[2]][j]=="-":
                    tablero[2][j]=="X"
                    cant_disparos+=1
                    
                if cant_disparos==barcos[0]:
                    barcos_dest+=1
                    
        
               
      
    








# OPCIONAL:
# Cambie el valor de esta variable a 1 si desea ver
# la ubicación de los barcos antes de comenzar.
# Esto puede ser útil para probar sus funciones.
mostrar_solucion = 1



##################################################
#                                                #
#  NO MODIFIQUE EL CÓDIGO A PARTIR DE ESTE PUNTO #
#                                                #
##################################################

import random as rd

# Función que muestra el tablero con el formato deseado para la pantalla
def show(tablero):
    print("\n  123456789")
    for i in range(9):
        fila_texto = " "
        for j in tablero[i]:
            fila_texto += str(j)
        print(chr(65+i)+fila_texto)

# Creación del tablero (inicialmente únicamente con "-" en todas las posiciones)
tablero = []
board = []
for i in range(9):
    fila = []
    for j in range(9):
        fila.append("-")
    tablero.append(fila)
    board.append(list(fila))

# Creación de los barcos con orientación y posición aleatorias
barcos = []
length = [2,3,3,4,5]
for i in range(5):
    l = length[i]
    orientation = rd.randint(1,2)
    if orientation == 1:
        flag = True
        while flag:
            row = rd.randint(0,9-l)
            column = rd.randint(0,8)
            empty = True
            for j in range(l):
                empty = empty and board[row+j][column] != "X"
            if empty:
                flag = False
        for j in range(l): board[row+j][column] = "X"
    else:
        flag = True
        while flag:
            row = rd.randint(0,8)
            column = rd.randint(0,9-l)
            if "X" not in board[row][column:column+l]:
                flag = False
        for j in range(l): board[row][column+j] = "X"
    barcos.append([l,orientation,row,column])
print(barcos)
# Se muestra la solución al inicio en caso de que se haya seleccionado esta opción
if mostrar_solucion == 1:
    print("Solución:")
    show(board)
    print("\n\n")

# Ciclo principal del programa donde se reciben los disparos, se validan y se llama a la función disparo()
print("¡Bienvenido a Solitary Battleship!")
destroyed = 0
while destroyed < 5:
    not_valid = True
    while not_valid:
        turn = input("\n¿Que casilla desea disparar? (Ejemplo: A1): ")
        not_valid = False
        if len(turn) != 2:
            not_valid = True
            print("Ingrese una casilla válida por favor.")
        elif not("A" <= turn[0] and turn[0] <= "I"):
            not_valid = True
            print("Ingrese una casilla válida por favor.")
        elif not("1" <= turn[1] and turn[1] <= "9"):
            not_valid = True
            print("Ingrese una casilla válida por favor.")
        else:
            fila = "ABCDEFGHI".index(turn[0])
            columna = int(turn[1])-1
            if tablero[fila][columna] != "-":
                not_valid = True
                print("Ya ha disparado a esta casilla.")
    disparo(tablero, barcos, fila, columna)
    destroyed = destruidos(tablero, barcos)
    show(tablero)
    print("\n"+str(destroyed)+" barcos destruidos.")
    # Fin del juego
    if destroyed == 5:
        print("Felicidades, juego terminado.")
