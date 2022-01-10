import random
from coo import*
from tablero import *
import time 
def cambiarlancha(lis,coor,f0,c0,s):
          """PRE: ingresa una lista con el tablero del jugador, una lista con coordenadas y dos varaibles tipo coordenadas a agregar, y una variable tipo numerica que diferencia si es el jugador o el computador
             POST:agrega a el tablero y a coordenadas una kancha tactica """
          x=[]
          x.append(f0)
          x.append(c0)
          coor.append(x)
          lis[f0-1][c0-1]="B"
          if s==1:
                    agregar(f0,c0,"GREEN","WHITE")
          return lis,coor
def cambiaravion(lis,coor,s):
          """PRE:ingresa una lista con elementos del tablero del computador,otra con las coordenadas hasta el momento,y dos listas donde una contiene las filas y otra las columnas
             POST:retorna el tablero y la lista coordenadas modificadas"""
          c=8
          for x in range(4):
                    if s==1:
                              agregar(x+2,c,"ORANGE","WHITE")
                    lis[x+1][c-1]="B"
          for x in range (4):
                    va=[]
                    va.append(x+2)
                    va.append(c)
                    coor.append(va)
          return coor,lis
def cambiarbuques(lis,coor,f1,c1,s):
          """PRE:ingresa una lista vacia
             POST:retorna una lista con las coordenadas de todos los barcos del computador y el tablero del computador"""
          lis[f1-1][c1-1]="B"
          lis[f1-1][c1]="B"
          lis[f1-1][c1+1]="B"
          f=[f1]*3
          c=[c1,c1+1,c1+2]
          for x in range (len(f)):
                    va=[]
                    if s==1:
                           agregar(f[x],c[x],"BLUE","WHITE")   
                    va.append(f[x])
                    va.append(c[x])
                    coor.append(va)
          return coor,lis
def compu(lis,s):
          """PRE:ingresa una lista vacia
             POST:retorna una lista con las coordenadas de todos los barcos del computador y el tablero del computador"""
          coor=[]
          lis=[[0 for x in range(8)] for x in range(8)]
          for x in range(2):
                    f0=random.randint(1,8)
                    c0=1
                    if x==1:
                              while f0==coor[0][0] and c0==coor[0][1]:
                                        f0=random.randint(1,8)
                                        c0=random.randint(1,2)
                    lis,coor=cambiarlancha(lis,coor,f0,c0,s)
          for x in range(2):
                    f1=random.randint(1,8)
                    c1=random.randint(2,4)
                    if x==1:
                              c1=5
                              while f1==coor[2][0]:
                                        f1=random.randint(1,8)
                    coor,lis=cambiarbuques(lis,coor,f1,c1,s)
          coo,lis=cambiaravion(lis,coor,s)
          if s==1:
                    c=0
                    print("Tus coordenadas son:")
                    for x in range(len(coo)):
                              if 0<=x<=1 :
                                        if x==0:
                                                  print("Tus lanchas tacticas se encuentran en:")
                                                  if c==1:
                                                            print(c)
                                                            c+=1
                                                            print("FI:",coo[x][0],"CO:",coo[x][1])
                                                  c+=1
                                        else:
                                                  time.sleep(1)
                                                  if c==3:
                                                            print("FI:",coo[x][0],"CO:",coo[x][1])
                              if 1<x<=7:
                                        if x==2:
                                                  print("")
                                                  print("Tus buques de guerra se encuentran en:")
                                        if x==5:
                                                  print("")
                                        print("FI:",coo[x][0],"CO:",coo[x][1])
                                        time.sleep(1)
                              else:
                                        if x==8:
                                                  print("Tu portaaviones se encuentra en:")
                                        print("FI:",coo[x][0],"CO:",coo[x][1])
                                        time.sleep(1)
          time.sleep(5)
          return coor,lis
