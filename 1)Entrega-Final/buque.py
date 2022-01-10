from restricciones import *
from tablero import *
from aviones import*
def m(x):
          print("Tus coordenadas para tu buque de guerra",x+1,"son:"+"\n")
def repetir1(co,f,c,lis):
          """PRE:ingresa una lista con las coordenadas, dos variables tipo coordenadas, una lista con el tablero del jugador y una variable tipo tortuga
             POST:segun una variable ingresada por teclado se modifica el tablero o no"""
          print("")
          print("¿Desea cambiar sus coordenadas? Si/No")
          rta=sino()
          print("")
          if rta=="si":
                    if len(co)==2:
                              buque(co,lis,0,0)
                    else:
                              while rta!="no":
                                        rta,f,c=cambiar()
                              f,c=restricciones(f,c,lis)
                              return f,c,1
          return f,c,0
def utilizada():
          """PRE: no ingresa ningun parametro
             POST:muestra el error por el cual las coordenadas no son validas"""
          print("Existe una coordenada la cual ya está siendo utilizada por otro barco "+"\n")
          print("Vuelve a ubicar nuevas coordenadas, recuerda que se ocuparan tres casillas por buque "+"\n")
def cambiarconfilasig(lis,co,f1,c1,f3,c3,f,c):
    """PRE:una lista con las coordenadas del jugador y una del tablero del jugador e ingresa una lista de coordenadas de filas y otra de columnas 
       POST:modifica el tablero del jugador con los elementos de f, y hace un llamado a la función agregar"""
    lis[f1-1][c1-1]="B"
    lis[f1-1][c1]="B"
    lis[f3-1][c3-1]="B"
    for x in range(len(f)):
              agregar(f[x],c[x],"BLUE","WHITE")
    co=coor(f,c,co)
    return lis,co
def cambiarconcolig(lis,co,f1,c1,f3,c3,f,c):
    """PRE:una lista con las coordenadas del jugador y una del tablero del jugador e ingresa una lista de coordenadas de filas y otra de columnas 
       POST:modifica el tablero del jugador con los elementos de f, y hace un llamado a la función agregar"""
    lis      
    lis[f1-1][c1-1]="B"
    lis[f1][c1-1]="B"
    lis[f3-1][c3-1]="B"
    for x in range(len(f)):
              agregar(f[x],c[x],"BLUE","WHITE")
    co=coor(f,c,co)
    return lis,co
def buque(co,lis,v,vaa):
          """PRE:ingresa  una lista con las coordenadas de los dos primeros barcos y el tablero del jugador
             POST:retorna las listas modificadas por los nuevos barcos añadidos"""
          for x in range(2):
                    if v!=1 and vaa==0:
                              print("Buque de guerra ",x+1)
                    if len(co)==8:
                              break
                    print("Ingresa las coordenadas de donde ira la cabeza del barco")
                    f,c=imprimir()
                    f1,c1=restricciones(f,c,lis)
                    f1,c1,p=repetir1(co,f1,c1,lis)
                    rta=s()
                    f3,c3=sentido(rta,f1,c1,1)
                    if f1==f3:
                              if c1+2==c3 and c3-2==c1 and lis[f1-1][c1]!="B" and lis[f1-1][c3-1]!="B":
                                        vaa+=1
                                        m(x)
                                        f,c=[f1]*3,[c1,c1+1,c3]
                                        lis,co=cambiarconfilasig(lis,co,f1,c1,f3,c3,f,c)
                              elif c3+2==c1 and c1-2==c3 and lis[f3-1][c3]!="B" and lis[f3-1][c3-1]!="B":
                                        vaa+=1
                                        m(x)
                                        f,c=[f1]*3,[c3,c3+1,c1]
                                        lis,co=cambiarconfilasig(lis,co,f1,c3,f3,c1,f,c)
                              else:
                                        utilizada()
                                        if x==0 and len(co)==2:
                                                   buque(co,lis,0,0) 
                                        else:
                                                  vaa+=1
                                                  buque(co,lis,1,vaa)                   
                    elif c1==c3:
                              if f1+2==f3 and f3-2==f1 and lis[f1][c1-1]!="B" and lis[f3-1][c1-1]!="B":
                                        vaa+=1
                                        m(x)
                                        f,c=[f1,f1+1,f3],[c1]*3
                                        lis,co=cambiarconcolig(lis,co,f1,c1,f3,c3,f,c)
                              elif f3+2==f1 and f1-2==f3 and lis[f3][c3-1]!="B" and lis[f3-1][c1-1]!="B":
                                        vaa+=1
                                        m(x)
                                        f,c=[f3,f3+1,f1],[c1]*3
                                        lis,co=cambiarconcolig(lis,co,f3,c1,f1,c3,f,c)
                              else:
                                        utilizada()
                                        if x==0 and len(co)==2:
                                                  buque(co,lis,0,0)
                                        else:
                                                  vaa+=1
                                                  buque(co,lis,1,vaa)     
          return co,lis
