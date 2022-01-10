from restricciones import *

"""1
PRE: no ingresa ningun parametro
POST:muestra el error por el cual las coordenadas no son validas"""

def long():
          print("Las coordenadas no tienen longitud 4,no son validas"+"\n"+"Borrando Coordenadas del Portaavion...."+"\n")
          print("Vuelve a ubicar las coordenadas del portaaviones desde cero, recuerda que se ocuparan cuatro casillas para este tipo de barco")
          print("")

"""2
PRE: no ingresa ningun parametro
POST:muestra el error por el cual las coordenadas no son validas"""

def utilizada():
           print("Existe una coordenada la cual ya esta siendo utilizada por otro barco"+"\n"+"Borrando Coordenadas de Portaaviones...."+"\n")
           print("Vuelve a ubicar las coordenadas del Portaaviones desde cero, No repitas coordenadas")
           print("")
           
"""3
PRE:ingresan una lista,con elementos del tablero actual del jugador
POST:segun una respuesta ingresada por teclado se deja el tablero actual o el tablero se modificar"""

def repetir3(co,lis):
          print("")
          print("¿Desea cambiar sus coordenadas? Si/No")
          rta=input().strip().lower()
          print("")
          while rta!="si" and rta!="no":
                    print("Ingrese Si/No")
                    rta=input()
          if rta=="si":
                    aviones(co,lis)
          print("")
          return 0

"""6
PRE:ingresa una lista con el tablero del jugador ,las coordenadas actuales,filas y columnas unas de la cabeza del barco y otra de la cola del barco,y dos listas más con las filas y columnas de donde ira el barco
POST:modifica el tablero y las coordenas con los datos que entraron"""
def cambiarconfilasig(lis,co,f1,c1,f4,c4,f,c):
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
          return lis,co

"""7
PRE:ingresa una lista con el tablero del jugador ,las coordenadas actuales,filas y columnas unas de la cabeza del barco y otra de la cola del barco,y dos listas más con las filas y columnas de donde ira el barco
POST:modifica el tablero y las coordenas con los datos que entraron"""
def cambiarconcolig(lis,co,f1,c1,f4,c4,f,c):
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
          return lis,co



"""6
PRE:ingresa una lista con las coordenadas actuales de los barcos junto al tablero de juego
POST:retorna ambas listas modificadas añadiendo el poortavion"""

def aviones(co,lis):
          print("Portaavion 1")
          print("Ingresa las coordenada de donde ira la cabeza del barco")
          f,c=imprimir()
          f1,c1=restricciones(f,c,lis)
          print("Ingresa las coordenadas hasta donde ira el barco")
          f,c=imprimir()
          f4,c4=restricciones(f,c,lis)
          repetir3(co,lis)
          while f1!=f4 and c1!=c4:
                    print("Las coordenadas ingresadas no son validas por la separación de estas, el barco debe tener posiciones adyacentes."+"\n"+"Borrando Coordenadas de Buque...."+"\n")
                    print("Vuelve a ubicar las coordenadas del portaavion, recuerda que se ocuparan cuatro casillas en el portaavion."+"\n")
                    return aviones(co,lis)
          print("Tus coordenadas para tu portaavion son:"+"\n")
          if f1==f4:
                              if c1+3==c4 and c4-3==c1 and lis[f1-1][c1]!="B" and lis[f1-1][c1+1]!="B":
                                        f=[f1]*4
                                        c=[c1,c1+1,c1+2,c4]
                                        lis,co=cambiarconfilasig(lis,co,f1,c1,f4,c4,f,c)
                                        tablero(lis)
                                        return co,lis
                              elif c4+3==c1 and c1-3==c4 and lis[f4-1][c4]!="B" and lis[f4-1][c4+1]!="B":
                                        f=[f1]*4
                                        c=[c4,c4+1,c4+2,c1]
                                        lis,co=cambiarconfilasig(lis,co,f1,c4,f4,c1,f,c)
                                        tablero(lis)
                                        return co,lis
                              elif c1+3!=c4 and c4-3!=c1 and c4+3!=c1 and c1-3!=c4:
                                        long()
                                        tablero(lis)
                                        aviones(co,lis)
                                        
                              else:
                                        utilizada()
                                        tablero(lis)
                                        aviones(co,lis)
          elif c1==c4:
                    if f1+3==f4 and f4-3==f1 and lis[f1][c1-1]!="B" and lis[f1+1][c1-1]!="B":
                              f=[f1,f1+1,f1+2,f4]
                              c=[c1]*4
                              lis,co=cambiarconcolig(lis,co,f1,c1,f4,c4,f,c)
                              tablero(lis)
                              return co,lis
                    elif f4+3==f1 and f1-3==f4 and lis[f4][c4-1]!="B" and lis[f4+1][c4-1]!="B":
                              f=[f4,f4+1,f4+2,f1]
                              c=[c1]*4
                              lis,co=cambiarconcolig(lis,co,f4,c1,f1,c4,f,c)
                              tablero(lis)
                              return co,lis
                    elif f1+3!=f4 and f4-3!=f1 and f4+3!=f1 and f1-3!=f4:
                              long()
                              tablero(lis)
                              aviones(co,lis)
                                        
                    else:
                              utilizada()
                              tablero(lis)
                              aviones(co,lis)        
          return co,lis
