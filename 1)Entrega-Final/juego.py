from restricciones import *
from tablero import *
from interfaz import *
import random
import turtle
def ata(t,disp,f,c,x,y):
          """PRE:ingresa una variable tipo tortuga, una variable disp que dice si hay un barco o no en el tablero y 2 pares de variables tipo coordenadas
             POST:modifica el interfaz grafico ya sea con la funcion xx o vacio"""
          f,c=x+(50*(c-1)),y-(50*(f-1))
          if disp==1:
                    xx(f,c,x,y)
                    t.color("BLACK")
          else:
                    vacio(f,c,x,y)
                    t.color("BLACK")
def ataques(lis,f,c,computador,t,cont):
          """PRE:ingresa una lista con el tablero del jugador una variable tipo fila y otra columna, una variable tipo contador
             POST: modifica el tablero segun la fila y columna ingresada con - o X"""
          while lis[f-1][c-1]=="B":
                    lis[f-1][c-1]="X"
                    ata(t,1,f,c,-400,200)
                    print("Le dieron a un barco Tuyo")
                    f,c=random.randint(1,8),random.randint(1,8)
                    while lis[f-1][c-1]=="-" or lis[f-1][c-1]=="X":
                              f,c=random.randint(1,8),random.randint(1,8)
                    computador+=1
          while lis[f-1][c-1]=="-" or lis[f-1][c-1]=="X" or lis[f-1][c-1]=="B":
                    f,c=random.randint(1,8),random.randint(1,8)
          ata(t,0,f,c,-400,200)
          lis[f-1][c-1]="-"
          return lis,computador
          

def restriccion(f,c,lis):
          """PRE:ingresa una variable tipo columna y otra tipo fila,una lista que contiene el tablero del jugador
             POST:retorna la fila y columna sin incumplir alguna restricción"""
          while f>8 or c>8 or f==0 or c==0:
                    if f<=0 or c<=0 or f>8 or c>8:
                              print("las coordenadas se salen del rango 1-8")
                              f,c=filycol()
          while  lis[f-1][c-1]=="-" or lis[f-1][c-1]=="X":
                    if lis[f-1][c-1]=="-" or lis[f-1][c-1]=="X":
                              print("Disparo ya realizado, por favor no repita coordenadas")
                              f,c=filycol()
                              while f>8 or c>8 or lis[f-1][c-1]=="-" or lis[f-1][c-1]=="X":
                                        while f>8 or c>8 or f<=0 or c<=0:
                                                  print("las coordenadas se salen del rango 1-8")
                                                  f,c=filycol()
                                                  print("las coordenadas se salen del rango 1-8")
                                        while lis[f-1][c-1]=="-" or lis[f-1][c-1]=="X":
                                                  print("Disparo ya realizado, por favor no repita coordenadas")
                                                  f,c=filycol()
                                                  while f>8 or c>8 or f<=0 or c<=0:
                                                            print("las coordenadas se salen del rango 1-8")
                                                            f,c=filycol()
                    return f,c
          return f,c
def juego(lis,lis2,pos,di,co2):
          """PRE:ingresa una lista con el tablero del jugador,una lista con el tablero del computador,una variable tipo dificultad,y una lista simulando el tablero oculto del computador
             POST:retorna el ganador del juego"""
          jugador=0
          computador=0
          coo=co2[:]
          c,t=1,turtle.Turtle()
          while jugador<=12 and computador<=12:
                    print("")
                    print("El Jugador lleva:",jugador,"Puntos")
                    print("El Computador lleva:",computador,"Puntos")
                    print("")
                    if jugador==12 or computador==12:
                              if jugador==12:
                                        x="Jugador"
                                        return x
                              else:
                                        x="Computador"
                                        return x
                    print("Ingrese la posición que desea atacar")
                    f,c=imprimir()
                    f,c=restriccion(f,c,lis2)
                    h=0
                    while lis2[f-1][c-1]=="B":
                              avi()
                              time.sleep(1)
                              misi()
                              lis2[f-1][c-1]="X"
                              time.sleep(2)
                              explocion()
                              print("BUMMM!!!!, le diste a un barco"+"\n")
                              ata(t,1,f,c,50,200)
                              f,c=filycol()
                              f,c=restriccion(f,c,lis2)
                              h+=1
                              jugador+=1
                    if h>=1:
                              avi()
                              time.sleep(1)
                              misi()
                              time.sleep(2)
                              ata(t,0,f,c,50,200)
                              lis2[f-1][c-1]="-"
                              print("Fallaste, cambiando de turno")
                    elif h==0:
                              avi()
                              time.sleep(1)
                              misi()
                              time.sleep(2)
                              ata(t,0,f,c,50,200)
                              print("Fallaste, cambiando de turno")
                              lis2[f-1][c-1]="-"
                    print("El computador esta atacando......")
                    if di==1:
                              f,c=random.randint(1,8),random.randint(1,8)
                              while lis[f-1][c-1]=="-" or lis[f-1][c-1]=="X":
                                        f,c=random.randint(1,8),random.randint(1,8) 
                              if lis[f-1][c-1]=="B":
                                        lis,computador=ataques(lis,f,c,computador,t,computador)
                              else:
                                        ata(t,0,f,c,-400,200)
                                        print("El computador fallo, cambiando de turno")
                                        lis[f-1][c-1]="-"
                    else:
                              f,c=random.randint(1,8),random.randint(1,8)
                              o=0
                              while lis[f-1][c-1]=="-" or lis[f-1][c-1]=="X":
                                                  f,c=random.randint(1,8),random.randint(1,8)
                              if o%5==0 and len(coo)>=1:
                                        f,c=coo[0][0],coo[0][1]
                                        del coo[0]
                              if lis[f-1][c-1]=="B":
                                        if o%2==0:
                                                  if len(coo)>=1:
                                                            f,c=coo[0][0],coo[0][1]
                                                            del coo[0]
                                                            o+=1
                                                            lis,computador=ataques(lis,f,c,computador,t,computador)              
                                                  else:
                                                            lis,computador=ataques(lis,f,c,computador,t,computador)
                                        else:
                                                  o+=1
                                                  lis,computador=ataques(lis,f,c,computador,t,computador)
                              else:
                                        ata(t,0,f,c,-400,200)
                                        print("El computador fallo, cambiando de turno")
                                        lis[f-1][c-1]="-"
          return x
