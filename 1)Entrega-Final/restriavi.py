from buque import *
from coo import *
def utilizada():
          """PRE: no ingresa ningun parametro
             POST:muestra el error por el cual las coordenadas no son validas"""
          print("Existe una coordenada la cual ya esta siendo utilizada por otro barco "+"\n"+"Borrando Coordenadas de Buque...."+"\n")
          print("Vuelve a ubicar nuevas coordenadas  , recuerda que se ocupara cuatro para el portavion "+"\n"+"\n")
def s():
          print("Ingrese la (1,2,3,4) según quiera el sentido del barco:"+"\n"+"1.Arriba."+"\n"+"2.Abajo."+"\n"+"3.Izquierda."+"\n"+"4.Derecha."+"\n")
          rta=input().strip()
          while rta!="1" and rta!="2" and rta!="3" and rta!="4":
                    print("Ingrese (1,2,3,4) segun corresponda")
                    rta=input().strip()
                    print("")
          return rta
def coor(f,c,co):
          """PRE:ingresan dos listas una con las filas ingresadas y otra con las columnas ingresadas
             POST:muestra en pantalla las coordenadas ingresadas por el usuario"""
          for x in range (len(f)):
                    print("Fil:",f[x],"Col:",c[x])
                    va=[]
                    va.append(f[x])
                    va.append(c[x])
                    co.append(va)
          return co
def sino():
          """PRE:no se recibe ningun argumento
             POST:retorna una respuesra SI/NO para realizar dos acciones diferentes"""
          rta=input().strip().lower()
          while rta!="si" and rta!="no":
                    print("Ingrese Si/No")
                    rta=input().strip().lower()
          return rta
def numeros(f,c):
          """PRE:ingresan dos variables
             POST: retorna las dos variable tipo numericas"""
          abc="+abcdefghijklmnopqrstuvwxyz.,-[]*¨´?¡=^\/()<!>&"
          ABC=abc.upper()
          while len(f)==0 or len(c)==0 or " " in f or " " in c:
                    print("Ingrese valores numericos:")
                    f=input("Fil:")
                    c=input("Col:")
          while f[0] in abc or f[0] in ABC or c[0] in abc or c[0] in ABC:
                    print("Ingrese valores numericos:")
                    f=input("Fil:")
                    c=input("Col:")
          return int(f),int(c)
def imprimir():
          """PRE:no se recibe ningun parametro
             POST:Hace un llamado a la función nuemros y retorna dos variables una tipo fila y otra tipo columna"""
          f=input("Fil:")
          c=input("Col:")
          f,c=numeros(f,c)
          return f,c
def filycol():
          """PRE:no ingresa ningun parametro
             POST:retorna fila y columna que se usaran, ingresadas por teclado """
          print("Ingrese nuevas coordenadas:")
          f,c=imprimir()
          return f,c
def rang():
          """PRE:no recibe ningun argumento
             POST:retorna una variable tipo sentido ingresada por teclado"""
          print("favor cambiar de sentido, puesto que se sale del rango del tablero")
          print("Ingrese (1,2,3,4) según corresponda:"+"\n")
          rta=input().strip()
          return rta                    

def sentido(rta,f,c,tipo):
          """PRE:ingresa una variable tipo sentido dos variables tipo coordenada fil y col respectivamente y una variable tipo de clasificación de barco
             POST:retorna la f y col que cumpla la posición final deseada del sentido"""
          if rta=="1":
                    if f-1-tipo<1:
                              rta=rang()
                              return sentido(rta,f,c,tipo)
                    f=f-1-tipo
                    return f,c
          elif rta=="2":
                    if f+1+tipo>8:
                              rta=rang()
                              return sentido(rta,f,c,tipo)
                    f=f+1+tipo
                    return f,c
          elif rta=="3":
                    if c-1-tipo<1:
                              rta=rang()
                              return sentido(rta,f,c,tipo)
                    c=c-1-tipo
                    return f,c
          else:
                    if c+1+tipo>8:
                              rta=rang()
                              return sentido(rta,f,c,tipo)
                    c=c+1+tipo
                    return f,c
def restricciones(f,c,lis):
          """PRE:ingresa dos variables tipo coordenadas fil y col respectivamente y una lista con el tablero del jugador
             POST:retorna las dos variables tipo coordenadas restringidas por varias condiciones dadas"""
          while f>8 or c>8 or c<=0 or f<=0:
                    f,c=filycol()
          while  lis[f-1][c-1]=="B" :
                    if lis[f-1][c-1]=="B":
                              print("")
                              print("Coordenadas ya ocupadas por otro barco, Ingrese Nuevas coordenadas."+"\n")
                              f,c=filycol()
                              while f>8 or c>8 or f<=0 or c<=0:
                                        f,c=filycol()
          return f,c
