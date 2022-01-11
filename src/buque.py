from restricciones import *


"""1
PRE: no ingresa ningun parametro
POST:muestra el error por el cual las coordenadas no son validas"""

def utilizada():
          print("Existe una coordenada la cual ya esta siendo utilizada por otro barco o las coordenadas NO son adyacentes"+"\n"+"Borrando Coordenadas de Buque...."+"\n")
          print("Vuelve a ubicar los buques de guerra, recuerda que se ocuparan tres casillas por buque  o NO repitas  cordenadas."+"\n")
          
"""2
PRE: no ingresa ningun parametro
POST:muestra el error por el cual las coordenadas no son validas"""


def long2():
          print("Las coordenadas no tienen longitud 3,no son validas"+"\n"+"Borrando Coordenadas de Buque...."+"\n")
          print("Vuelve a ubicar las coordenadas del buque de guerra desde cero, recuerda que se ocuparan tres casillas por buque")
          print("")
"""3
PRE:ingresa el tablero del jugador, y las coordenadas actuales del jugador, una variable tipo numerica
POST:retorna las dos listas modificadas borrando coordenadas y barcos no deseados por el usuario"""

def subborrar(lis,co,f):
    for x in range(1,f):
        lis[co[len(co)-x][0]-1][co[len(co)-x][1]-1]=0
    for j in range(1,f):
        del co[len(co)-1]
    return co,lis

"""4
PRE:Ingresa una lista de las coordenadas actuales y la lista con elementos del tablero del jugador
POST:retorna una lista de coordenadas sin algunos elementos y el tablero modificado.(para cambiar coordenadas)"""

def borrar(co,lis):
           if len(co)==2:
                     return co,lis
           else:
                    co,lis=subborrar(lis,co,len(co)-1)
                    tablero(lis)
                    return co,lis
                
"""5
PRE: ingresa las coordenadas actuales del usuario y el tablero de juego
POST:dependiendo de la respuesta por teclado llama a la funcion borrar o no"""

def repetir2(co,lis):
          print("")
          print("¿Desea cambiar sus coordenadas? Si/No")
          rta=input().strip().lower()
          print("")
          while rta!="si" and rta!="no":
                    print("Ingrese Si/No")
                    rta=input()
          if rta=="si":
                    if len(co)!=2:
                              co,lis=borrar(co,lis)
                              print("Borrando coordenadas..."+"\n")
                    print("Ingrese de nuevo las Coordenadas para:"+"\n")
                    buque(co,lis)
          print("")
          return 0



"""6
PRE:
POST:"""
def cambiarconfilasig(lis,co,f1,c1,f3,c3,f,c):
    lis[f1-1][c1-1]="B"
    lis[f1-1][c1]="B"
    lis[f3-1][c3-1]="B"
    for x in range (len(f)):
        print("Fil:",f[x],"Col:",c[x])
        va=[]
        va.append(f[x])
        va.append(c[x])
        co.append(va)
    return lis,co

"""7
PRE:
POST:"""
def cambiarconcolig(lis,co,f1,c1,f3,c3,f,c):
    lis[f1-1][c1-1]="B"
    lis[f1][c1-1]="B"
    lis[f3-1][c3-1]="B"
    for x in range (len(f)):
        print("Fil:",f[x],"Col:",c[x])
        va=[]
        va.append(f[x])
        va.append(c[x])
        co.append(va)
    return lis,co




"""8
PRE:ingresa  una lista con las coordenadas de los dos primeros barcos y el tablero del jugador
POST:retorna las listas modificadas por los nuevos barcos añadidos"""

def buque(co,lis):
          for x in range(2):
                    print("Buque de guerra ",x+1)
                    print("Ingresa las coordenada de donde ira la cabeza del barco")
                    f,c=imprimir()
                    f1,c1=restricciones(f,c,lis)
                    print("Ingresa las coordenadas hasta donde ira la cola del barco")
                    f,c=imprimir()
                    f3,c3=restricciones(f,c,lis)
                    repetir2(co,lis)
                    while f1!=f3 and c1!=c3:
                              long2()
                              co,lis=borrar(co,lis)
                              return buque(co,lis)
                    print("Tus coordenadas para tu buque de guerra",x+1,"son:"+"\n")
                    if f1==f3:

                              if c1+2==c3 and c3-2==c1 and lis[f1-1][c1]!="B":
                                        f=[f1]*3
                                        c=[c1,c1+1,c3]
                                        lis,co=cambiarconfilasig(lis,co,f1,c1,f3,c3,f,c)
                                        tablero(lis)
                              elif c3+2==c1 and c1-2==c3 and lis[f3-1][c3]!="B":
                                        f=[f1]*3
                                        c=[c3,c3+1,c1]
                                        cambiarconfilasig(lis,co,f1,c3,f3,c1,f,c)
                                        tablero(lis)
                              elif c1+2!=c3 and c3-2!=c1 and c3+2!=c1 and c1-2!=c3:
                                        long2()
                                        co,lis=borrar(co,lis)
                                        tablero(lis)
                                        return buque(co,lis)
                              else:
                                        utilizada()
                                        co,lis=borrar(co,lis)
                                        tablero(lis)
                                        return buque(co,lis)
                    elif c1==c3:
                              if f1+2==f3 and f3-2==f1 and lis[f1][c1-1]!="B":
                                        f=[f1,f1+1,f3]
                                        c=[c1]*3
                                        lis,co=cambiarconcolig(lis,co,f1,c1,f3,c3,f,c)
                                        tablero(lis)
                              elif f3+2==f1 and f1-2==f3 and lis[f3][c3-1]!="B":
                                        f=[f3,f3+1,f1]
                                        c=[c1]*3
                                        lis,co=cambiarconcolig(lis,co,f3,c1,f1,c3,f,c)
                                        tablero(lis)
                              elif f1+2!=f3 and f3-2!=f1 and f3+2!=f1 and f1-2!=f3:
                                        long2()
                                        co,lis=borrar(co,lis)
                                        tablero(lis)
                                        return buque(co,lis)
                              else:
                                        utilizada()
                                        co,lis=borrar(co,lis)
                                        tablero(lis)
                                        return buque(co,lis)
                    
          return co,lis
                    
                              
