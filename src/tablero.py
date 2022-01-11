import math
import turtle

#para mi x de referencia sera -400 , mi y de referencia sera 200
#     1 2 3 4 5 6 7 8 " 1 2 3 4 5 6 7 8
# 200 1 - - - - - - -   - - - - - - - -
# 150 2 - - - - - - -   - - - - - - - -
# 50  3 - - - - - - -   - - - - - - - -
# 0   4 - - - - - - -   - - - - - - - -
#-50  5 - - - - - - -   - - - - - - - -
#-100 6 - - - - - - -   - - - - - - - -
#-150 7 - - - - - - -   - - - - - - - -
#-200 8 - - - - - - -   - - - - - - - -
#  (-400)---------(-50)-(50)---------(400)
def mov(x,y,t):
          """PRE:ingresan dos variables tipos coordenadas y una tipo tortuga
             POST:la tortuga se desplaza a las coordenadas ingresadas"""
          t.penup()
          t.goto(x,y)
          t.pendown()
def vacio(f,c,x,y):
          t=turtle.Turtle()
          t.speed(4)
          mov(f,c,t)
          t.seth(270)
          t.fd(25)
          t.seth(0)
          t.color("BLACK")
          t.pensize(5)
          t.fd(50)
          mov(x,y,t)
          t.pensize(0)
def xx(f,c,x,y):
          t=turtle.Turtle()
          t.speed(4)
          mov(f,c,t)
          t.color("RED")
          t.pensize(5)
          t.seth(315)
          t.fd(50*(math.sqrt(2)))
          t.backward((50*(math.sqrt(2)))//2)
          t.seth(45)
          t.backward((50*(math.sqrt(2)))//2)
          t.fd(50*(math.sqrt(2)))
          t.seth(0)
          mov(x,y,t)
          t.color("BLACK")
          t.pensize(0)
def num(t,x,y,n,pal,xx,yy,col):
          """PRE: ingresa una variable tipo tortuga ,dos pares de variables tipo de coordenadas,una tipo cadena y otra tipo color
             POST:muestra en pantalla las f y c en un rango 1-8 y escpecifica si es tablero del jugador o del enemigo """
          mov(x,y,t)
          t.speed(8)
          t.color(col)
          t.write(pal,False,"right", ("arial", 20, "bold italic"))
          for a in range(n):
                    mov(xx,yy,t)
                    t.write("C"+str(a+1), False,"right", ("arial", 15, "bold italic"))
                    xx+=50
          xx=xx-(50*8)-10
          xx-=30
          yy-=30
          for a in range(n):
                    mov(xx,yy,t)
                    t.write("F"+str(a+1), False,"right", ("arial", 15, "bold italic"))
                    yy-=50
def tablero(x,y,t):
          """PRE:entran dos variables tipo coordenadas y una variable tipo tortuga
             POST:Se crea el un tablero de juego y se hace un ll"""
          t.speed(8)
          mov(x,y,t)
          for a in range(4):
                    t.fd(400)
                    t.left(90)
          for a in range(4):
                    t.fd(50)
                    t.left(90)
                    t.fd(400)
                    t.seth(0)
                    t.fd(50)
                    t.seth(270)
                    t.fd(400)
                    t.seth(0)
          for a in range(4):
                    t.seth(90)
                    t.fd(50)
                    t.left(90)
                    t.fd(400)
                    t.seth(90)
                    t.fd(50)
                    t.seth(0)
                    t.fd(400)
def ubi(t,col,borde):
          t.color(col)
          t.pencolor(borde)
          t.begin_fill()
          for x in range(4):
                    t.fd(50)
                    t.right(90)
          t.end_fill()
          mov(-400,200,t)
def agregar(f,c,col,borde,):
          t=turtle.Turtle()
          t.speed(9)
          mov(-400,200,t)
          f,c=-400+(50*(c-1)),200-(50*(f-1))
          mov(f,c,t)
          ubi(t,col,borde)
          mov(-400,200,t)
def crear():
          t=turtle.Turtle()
          tablero(-400,-200,t)
          tablero(50,-200,t)
          num(t,-150,250,8,"Tu Tablero",-370,200,"BlACK")
          num(t,300,250,8,"Tablero Enemigo",80,200,"BLUE")
          mov(-400,200,t)
          
