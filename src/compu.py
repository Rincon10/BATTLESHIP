import random

from coo import*

"""1
PRE:ingresa una lista con elementos del tablero del computador,otra con las coordenadas hasta el momento,y dos listas donde una contiene las filas y otra las columnas
POST:retorna el tablero y la lista coordenadas modificadas"""
def cambiaravion(lis,coor):
          c=8
          for x in range(4):
                    lis[x+1][c-1]="B"
          for x in range (4):
                    va=[]
                    va.append(x+2)
                    va.append(c)
                    coor.append(va)
          return coor,lis


"""2
PRE:ingresa una lista con elementos del tablero del computador,otra con las coordenadas hasta el momento,y dos listas donde una contiene las filas y otra las columnas
POST:retorna el tablero y la lista coordenadas modificadas"""
def cambiarbuques(lis,coor,f,c,f1,c1):
          lis[f1-1][c1-1]="B"
          lis[f1-1][c1]="B"
          lis[f1-1][c1+1]="B"
          f=[f1]*3
          c=[c1,c1+1,c1+2]
          for x in range (len(f)):
                    va=[]
                    va.append(f[x])
                    va.append(c[x])
                    coor.append(va)
          return coor,lis
          
"""3
PRE:ingresa una lista vacia
POST:retorna una lista con las coordenadas de todos los barcos del computador y el tablero del computador"""

def compu(lis):
          coor=[]
          for f in range(8):
                    va=[]
                    for c in  range(8):
                              va.append(0)
                    lis.append(va)
          for x in range(2):
                    f0=random.randint(1,8)
                    c0=1
                    if x==1:
                              while f0==coor[0][0] and c0==coor[0][1]:
                                        f0=random.randint(1,8)
                                        c0=random.randint(1,2)
                    lis,coor=añadir(lis,coor,f0,c0)
          for x in range(2):
                    f1=random.randint(1,8)
                    c1=random.randint(2,4)
                    if x==1:
                              c1=5
                              while f1==coor[2][0]:
                                        f1=random.randint(1,8)
                    coor,lis=cambiarbuques(lis,coor,f,c,f1,c1)
          coo,lis=cambiaravion(lis,coor)          
          return coor,lis
