"""1
PRE:ingresan dos variables
Post: retorna las dos variable tipo numericas"""

def numeros(f,c):
          abc="abcdefghijklmnopqrstuvwxyz.,-[]+¨´?¡=?()<!>&"
          ABC=abc.upper()
          while f in abc or f in ABC or c in abc or c in ABC:
                    print("Ingrese valores numericos:")
                    f=input("Fil:")
                    c=input("Col:")
          return int(f),int(c)

"""2
PRE:no se recibe ningun parametro
POST:Hace un llamado a la función nuemros y retorna dos variables una tipo fila y otra tipo columna"""

def imprimir():
          f=input("Fil:")
          c=input("Col:")
          f,c=numeros(f,c)
          return f,c
          

"""3
PRE:ingresa una lista del tablero del jugador
POST:muestra la lista (tablero) sin espacios"""

def mostrar(m):
    rta=""
    for x in range(len(m)):
        for j in range(len(m)):
            if j==0:
                rta=rta+str(m[x][j])
            else:
                rta=rta+","+str(m[x][j])
        rta=rta+"]"+"\n"+"["
    rta="["+rta
    print(rta[0:len(rta)-2])

"""4
PRE:no ingresa ningun parametro
POST:retorna fila y columna que se usaran, ingresadas por teclado """

def filycol():
          print("Coordenadas no validas para Fil y Col, ingrese un numero en el rango de 1-8.")
          f,c=imprimir()
          return f,c

"""5
PRE:no ingresa ningun parametro
POST:retorna la fila del tablero que usara,ingresada por teclado """
def fil():
           print("Coordenada no valida para Fil, ingrese un numero en el rango de 1-8.")
           f=input("Fil:")
           abc="abcdefghijklmnopqrstuvwxyz.,-[]+¨´?¡=?()"
           ABC=abc.upper()
           while f in abc or f in ABC :
                    print("Ingrese valores numericos:")
                    f=input("Fil:")
           return int(f)

"""6
PRE:no ingresa ningun parametro
POST:retorna la columna del tablero que usara,ingresada por teclado """
def col():
          
          print("Coordenada no valida para Col, ingrese un numero en el rango de 1-8.")
          c=input("Col:")
          abc="abcdefghijklmnopqrstuvwxyz.,-[]+¨´?¡=?()"
          ABC=abc.upper()
          while c in abc or c in ABC:
                    print("Ingrese valores numericos:")
                    f=input("Fil:")
                    c=input("Col:")
          return int(c)


"""7
PRE:ingresa una lista con el tablero del jugador
POST:muestra las condiciones definidas en el codigo de la funcion
"""
def tablero(lis):
          print("")
          print("Tu tablero es:"+"\n")
          mostrar(lis)
          print("")

"""8
PRE:ingresa una lista con el tablero del jugador
POST:muestra las condiciones definidas en el codigo de la funcion
"""

def Tenemigo(lis):
          print("")
          print("Tablero enemigo:"+"\n")
          mostrar(lis)
          print("")

"""9
PRE:ingresan dos listas una la tabla del usuario y la tabla del computador
POST:llama a dos funciones diferentes y muestra o imprime lo que esta descrito en la función"""
def tablas(lis1,lis2):
          Tenemigo(lis2)
          print("/--/--/--/--/--/")
          tablero(lis1)

def restricciones(f,c,lis):
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
          while  lis[f-1][c-1]=="B" :
                    if lis[f-1][c-1]=="B":
                              print("Coordenadas ya ocupadas por otro barco, Ingrese Nuevas coordenadas.")
                              f,c=imprimir()
                              while f>8 or c>8:
                                        if f>8 and c>8:
                                                  f,c=filycol()
                                        elif f>8:
                                                  f=fil()
                                        else:
                                                  c=col()
          return f,c
