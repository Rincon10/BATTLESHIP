import os

from compu import *

from interfaz import *

from tablero import *

from coo import *

from juego import*

def main():
          inicio()
          c=0
          di=input().strip()
          while di!="1" and di!="2":
                    print("Ingrese el numero 1 o 2.")
                    di=input()
          lis,lisi,di=[],[],int(di)
          if di==1:
                    h="Classic"
                    print("Elegiste la dificultad",h)
          else:
                    h="Advanced"
                    print("Elegiste la dificultad",h)
          pos,lis=coord(lis)
          c=1
          if c==1:
                    ini()
                    print("")
                    print("Espere unos segundos la maquina esta acomodando sus barcos")
                    print("")
                    print("Sabias que..."+"\n"+"\n"+"En la víspera de Navidad en 1914,en plena primera guerra mundial los soldados de ambos lados del frente occidental cantaron villancicos entre sí el día de Navidad, Las tropas a lo largo de dos tercios del Frente declararon una tregua fue tanto asi, que en algunos lugares la tregua duró una semana.Un año más tarde, los centinelas de ambos lados recibieron la orden de disparar a cualquiera que intentara repetir su actuación."+"\n")
                    for x in range(1,100000199):
                              y=1
                    for x in range(8):
                              va=[]
                              for x in range(8):
                                        va.append(0)
                              lisi.append(va)
                    ini1()
                    for x in range(1,100000199):
                              y=1
                    lis2=[]
                    pos2,lis2=compu(lis2)
                    print("Que empiece la guerra!!")
                    ganador=juego(lis,lis2,pos,di,lisi)
                    print("El ganador fue:",ganador)
                    
                    
main()
