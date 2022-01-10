from buque import*
from aviones import *
from restricciones import*
from tablero import *
import turtle
def repetir(co,f,c,lis):
          print("")
          print("¿Desea cambiar sus coordenadas? Si/No")
          rta=sino()
          print("")
          if rta=="si":
                    if len(co)==0:
                              lis=[]
                              coord(lis)
                    else:
                              while rta!="no":
                                        rta,f,c=cambiar()
                              f0,c0=restricciones(f,c,lis)
                              return f0,c0,1
          else:
                     return f,c,0
def añadir(lis,coor,f0,c0):
          """PRE: ingresan dos listas una de coordenadas ingresadas y otra del tablero de juego
             POST:añade la f0 y c0 a la lista coo y en esas posiciones cambia en lis por una B """ 
          x=[]
          x.append(f0)
          x.append(c0)
          coor.append(x)
          lis[f0-1][c0-1]="B"
          agregar(f0,c0,"GREEN","WHITE")
          return lis,coor
def lancha(co,x,p,lis):
          """PRE:ingresa una lista con las coordenadas  ya ingresadas por el jugador ,una variable tipo contador, una variable tipo numerica y la lista la cual contiene el tablero del jugador
             POST:se hace llamado a funciones como restricciones y añade las fil t col que cumplan las condiciones a lis y co"""
          f,c=imprimir()
          f0,c0=restricciones(f,c,lis)
          f0,c0,p=repetir(co,f0,c0,lis)
          print("Tus Coordenadas son:"+"\n"+"Fil:",str(f0)+"\n"+"Col:",str(c0)+"\n"+"para tu Lancha táctica",x+1)
          print("")
          lis,co=añadir(lis,co,f0,c0)
          return lis,co,p
def coord(lis):
          """PRE:Ingresa una lista vacia
             POST:retorna una lista con las coordenadas de las lanchas tacticas,buques de guerra y portaaviones ingresadas por el jugador y como esta el tablero de juego actualmente"""
          coor=[]
          lis=[[0 for x in range(8)] for x in range(8)]
          print("Ingrese las filas y columnas para acomodar tácticamente los barcos, primero empezaremos con las lanchas tácticas, recuerda que ocupan solo una casilla."+"\n")
          for x in range(2):
                    print("Lancha táctica",x+1)
                    lis,coor,p=lancha(coor,x,0,lis)
                    if p==1:
                              break
          print("")
          print("Ahora ubicaremos los buques de guerra, recuerda que se ocuparan tres casillas por buque."+"\n")
          co,lis=buque(coor,lis,0,0)
          print("")
          print("Ahora ubicaremos el Portaaviones, recuerda que se ocuparan cuatro casillas para esta gran nave."+"\n")
          coo,liss=aviones(co,lis)
          return coo,liss
