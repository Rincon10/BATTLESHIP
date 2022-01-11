import json
from compu import *
from interfaz import *
from tablero import *
from coo import *
from juego import*
from restricciones import *



def main():
          inicio()
          c=0
          di=input().strip()
          while di!="1" and di!="2":
                    print("Ingrese el número 1 o 2.")
                    di=input()
          lis,di=[],int(di)
          if di==1:
                    h="Classic"
                    print("Elegiste la dificultad",h)
          else:
                    h="Advanced"
                    print("Elegiste la dificultad",h)
          print("")
          print("¿Desea que la maquina Ordene sus barcos de forma aleatorea? Si/no")
          rta=sino()
          print("")
          print("Se acaba de generar una nueva pestaña, favor  buscarla en la multitarea de  Python"+"\n"+"\n")
          crear()
          if rta=="no":
                    pos,lis=coord(lis)
                    
          else:
                    pos,lis=compu(lis,1)
          c=1
          if c==1:
                    print("")
                    print("Antes de continuar no gustaria saber si desea guardar sus coordenadas. Si/No")
                    rta=sino().strip()
                    if rta=="si":
                              datos=json.dumps(pos)
                              f= open('guardado.txt','w')
                              f.write(datos)
                              f.close()
                              #se acaba de crear un archivo .txt llamado guardado donde almacena las coordenadas ingresadas por el jugador
                              print("Coordenadas guardadas, Continuemos.")
                              time.sleep(2)
                    print("")
                    
                    ini()
                    time.sleep(2)
                    print("")
                    print("Espere unos segundos la maquina esta acomodando sus barcos")
                    print("")
                    print("¿Sabías que?..."+"\n"+"\n"+"En la víspera de Navidad en 1914,en plena primera guerra mundial los soldados de ambos lados del frente occidental cantaron villancicos entre sí el día de Navidad, Las tropas a lo largo de dos tercios del Frente declararon una tregua fue tanto asi, que en algunos lugares la tregua duró una semana.Un año más tarde, los centinelas de ambos lados recibieron la orden de disparar a cualquiera que intentara repetir su actuación."+"\n")
                    time.sleep(12)
                    ini1()
                    time.sleep(2)
                    lis2=[]
                    pos2,lis2=compu(lis2,0)
                    print("Que empiece la guerra!!"+"\n")
                    print("El primero en completar 12 puntos, ganara la batalla ")
                    ganador=juego(lis,lis2,pos,di,pos)
                    print("El ganador fue:",ganador)
                    if ganador.strip()=="Jugador":
                              win()
                    else:
                              lose()
                    
                    
main()
