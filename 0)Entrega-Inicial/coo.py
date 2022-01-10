from buque import*

from aviones import *

from restricciones import*


"""1
PRE: ingresan dos listas una de coordenadas ingresadas y otra del tablero de juego
PRE:añade la f0 y c0 a la lista coo y en esas posiciones cambia en lis por una B """ 
def añadir(lis,coor,f0,c0):
          x=[]
          x.append(f0)
          x.append(c0)
          coor.append(x)
          lis[f0-1][c0-1]="B"
          return lis,coor
          

"""2
PRE:ingresan una lista,con elementos del tablero actual del jugador
POST:segun una respuesta ingresada por teclado se deja el tablero actual o el tablero se modificar"""

def repetir(lis):
          print("")
          print("¿Desea cambiar sus coordenadas? Si/No")
          rta=input().strip().lower()
          print("")
          while rta!="si" and rta!="no":
                    print("Ingrese Si/No")
                    rta=input()
          if rta=="si":
                    lis=[]
                    coord(lis)
          print("")
          return 0

"""3
PRE:Ingresa una lista vacia
POST:retorna una lista con las coordenadas de las lanchas tacticas ingresadas por el jugador y como esta el tablero de juego actualmente"""

def coord(lis):
          coor=[]
          for f in range(8):
                    va=[]
                    for c in  range(8):
                              va.append(0)
                    lis.append(va)
          tablero(lis)
          print("Ingrese las filas y columnas para acomodar tacticamente los barcos, primero empezaremos con las lanchas tacticas, recuerda que ocupan solo una casilla.")
          for x in range(2):
                    print("Lancha tactica",x+1)
                    f,c=imprimir()
                    f0,c0=restricciones(f,c,lis)
                    repetir(lis)
                    print("Tus Coordenadas son:"+"\n"+"Fil:",str(f0)+"\n"+"Col:",str(c0)+"\n"+"para tu Lancha tactica",x+1)
                    print("")
                    lis,coor=añadir(lis,coor,f0,c0)
                    tablero(lis)
          print("Ahora ubicaremos los buques de guerra, recuerda que se ocuparan tres casillas por buque.")
          print("")
          co,lis=buque(coor,lis)
          print("Ahora ubicaremos el Portaaviones, recuerda que se ocuparan cuatro casillas para esta gran nave.")
          print("")
          coo,liss=aviones(co,lis)
          return coo,liss
