from restriavi import *
from tablero import *
def repetir1(co,f,c,lis,t):
          """PRE:ingresa una lista con las coordenadas, dos variables tipo coordenadas, una lista con el tablero del jugador y una variable tipo tortuga
             POST:segun una variable ingresada por teclado se modifica el tablero o no"""
          print("")
          print("¿Desea cambiar sus coordenadas? Si/No")
          rta=sino()
          print("")
          if rta=="si":
                    print("Ingrese nuevas coordenadas"+"\n")
                    aviones(co,lis)
                   
          else:
                     return f,c,0
def cambiarconfilasig(lis,co,f1,c1,f4,c4,f,c):
          """PRE:ingresa una lista con el tablero del jugador ,las coordenadas actuales,filas y columnas unas de la cabeza del barco y otra de la cola del barco,y dos listas más con las filas y columnas de donde ira el barco
             POST:modifica el tablero y las coordenas con los datos que entraron"""
          lis[f1-1][c1-1]="B"
          lis[f1-1][c1]="B"
          lis[f1-1][c1+1]="B"
          lis[f4-1][c4-1]="B"
          for x in range (len(f)):
                    print("Fil:",f[x],"Col:",c[x])
                    va=[]
                    va.append(f[x])
                    va.append(c[x])
                    co.append(va)
                    agregar(f[x],c[x],"ORANGE","WHITE")
          return lis,co
def cambiarconcolig(lis,co,f1,c1,f4,c4,f,c):
          """PRE:ingresa una lista con el tablero del jugador ,las coordenadas actuales,filas y columnas unas de la cabeza del barco y otra de la cola del barco,y dos listas más con las filas y columnas de donde ira el barco
             POST:modifica el tablero y las coordenas con los datos que entraron"""
          lis[f1-1][c1-1]="B"
          lis[f1][c1-1]="B"
          lis[f1+1][c1-1]="B"
          lis[f4-1][c4-1]="B"
          for x in range (len(f)):
                    print("Fil:",f[x],"Col:",c[x])
                    va=[]
                    va.append(f[x])
                    va.append(c[x])
                    co.append(va)
                    agregar(f[x],c[x],"ORANGE","WHITE")
          return lis,co
def aviones(co,lis):
          """PRE:ingresa una lista con las coordenadas actuales de los barcos junto al tablero de juego
             POST:retorna ambas listas modificadas añadiendo el poortavion"""
          print("Portaavion 1")
          print("Ingresa las coordenada de donde ira la cabeza del barco")
          f,c=imprimir()
          f1,c1=restricciones(f,c,lis)
          f1,c1,p=repetir1(co,f1,c1,lis,2)
          rta=s()
          f4,c4=sentido(rta,f1,c1,2)
          print("Tus coordenadas para tu portaavion son:"+"\n")
          if f1==f4:
                              if c1+3==c4 and c4-3==c1 and lis[f1-1][c1]!="B" and lis[f1-1][c1+1]!="B" and lis[f1-1][c4-1]!="B":
                                        f=[f1]*4
                                        c=[c1,c1+1,c1+2,c4]
                                        lis,co=cambiarconfilasig(lis,co,f1,c1,f4,c4,f,c)
                                        return co,lis
                              elif c4+3==c1 and c1-3==c4 and lis[f1-1][c1-2]!="B" and lis[f1-1][c1-3]!="B" and lis[f1-1][c4-1]!="B":
                                        f=[f1]*4
                                        c=[c4,c4+1,c4+2,c1]
                                        lis,co=cambiarconfilasig(lis,co,f1,c4,f4,c1,f,c)
                                        return co,lis      
                              else:
                                        utilizada()
                                        aviones(co,lis)
          elif c1==c4:
                    if f1+3==f4 and f4-3==f1 and lis[f1][c1-1]!="B" and lis[f1+1][c1-1]!="B" and lis[f4-1][c1-1]!="B":
                              f=[f1,f1+1,f1+2,f4]
                              c=[c1]*4
                              lis,co=cambiarconcolig(lis,co,f1,c1,f4,c4,f,c)
                              return co,lis
                    elif  f4+3==f1 and f1-3==f4 and lis[f1-2][c4-1]!="B" and lis[f1-3][c4-1]!="B" and lis[f1-4][c4-1]!="B":
                              f=[f4,f4+1,f4+2,f1]
                              c=[c1]*4
                              lis,co=cambiarconcolig(lis,co,f4,c1,f1,c4,f,c)
                              return co,lis
                    else:
                              utilizada()
                              aviones(co,lis)
          print("")
          return co,lis
