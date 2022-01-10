from restricciones import *

from interfaz import *

import random

"""1
PRE:ingresa una variable tipo columna y otra tipo fila,una lista que contiene el tablero del jugador
POST:retorna la fila y columna sin incumplir alguna restricción"""
def restriccion(f,c,lis):
          while f>8 or c>8 or f==0 or c==0:
                    if (f<=0 and c<=0) or (f>8 and c>8):
                              f,c=filycol()
                    elif f<=0:
                              f=fil()
                    elif c<=0:
                              c=col()
                    elif f>8:
                              f=fil()
                    else:
                              c=col()
          while  lis[f-1][c-1]=="-" or lis[f-1][c-1]=="X":
                    if lis[f-1][c-1]=="-" or lis[f-1][c-1]=="X":
                              print("Disparo ya realizado, por favor no repita ubicaciones")
                              f,c=imprimir()
                              while f>8 or c>8:
                                        if f>8 and c>8:
                                                  f,c=filycol()
                                        elif f>8:
                                                  f=fil()
                                        else:
                                                  c=col()
          return f,c


"""2
PRE:ingresa una lista con el tablero del jugador,una lista con el tablero del computador,una variable tipo dificultad,y una lista simulando el tablero oculto del computador
POST:retorna el ganador del juego"""
def juego(lis,lis2,pos,di,lisi):
          jugador=0
          computador=0 
          c=1
          while jugador<12 and computador<12:
                    if jugador==11 or computador==11:
                              if jugador==11:
                                        x="Jugador"
                                        return x
                              else:
                                        x="Computador"
                                        return x
                    tablas(lis,lisi)
                    print("Ingrese la posicion que desea atacar")
                    f,c=imprimir()
                    f,c=restriccion(f,c,lisi)
                    h=0
                    while lis2[f-1][c-1]=="B":
                              lisi[f-1][c-1]="X"
                              tablas(lis,lisi)
                              explosion()
                              print("BUMMM, le diste a un barco"+"\n")
                              f,c=imprimir()
                              f,c=restriccion(f,c,lisi)
                              h+=1
                              jugador+=1
                    lisi[f-1][c-1]="-"
                    if h==0:
                              print("Fallaste, cambiando de turno")
                              lisi[f-1][c-1]="-"
                              tablas(lis,lisi)
                    print("El computador esta atacando......")
                    if di==1:
                              f,c=random.randint(1,8),random.randint(1,8)
                              if lis[f-1][c-1]=="B":
                                        while lis[f-1][c-1]=="B":
                                                  lis[f-1][c-1]="X"
                                                  print("Le dieron a un barco Tuyo")
                                                  f,c=random.randint(1,8),random.randint(1,8)
                                                  while lis[f-1][c-1]=="-" or lis[f-1][c-1]=="X":
                                                            f,c=random.randint(1,8),random.randint(1,8)
                                                  computador+=1
                                        lis[f-1][c-1]="-"
                                        tablas(lis,lisi)
                              else:
                                        print("El computador fallo, cambiando de turno")
                                        lis[f-1][c-1]="-"
                    else:
                              p=0
                              f,c=random.randint(1,8),random.randint(1,8)
                              if lis[f-1][c-1]=="B":
                                        while lis[f-1][c-1]=="B":
                                                  lis[f-1][c-1]="X"
                                                  print("Le dieron a un barco Tuyo")
                                                  p+=1
                                                  if p%2==0:
                                                            f,c=random.randint(1,8),random.randint(1,8)
                                                            
                                                  else:
                                                            if p<len(pos):
                                                                      f,c=pos[p][0],pos[p][1]
                                                                      p+=1
                                                                      
                                                            else:
                                                                      f,c=random.randint(1,8),random.randint(1,8)
                                                  while lis[f-1][c-1]=="-" or lis[f-1][c-1]=="X":
                                                            f,c=random.randint(f,8),random.randint(c,1)
                                                  computador+=1
                                        lis[f-1][c-1]="-"
                                        tablas(lis,lisi)
                              else:
                                        print("El computador fallo, cambiando de turno")
                                        lis[f-1][c-1]="-"

