import turtle
def mov(x,y,t):
          t.penup()
          t.goto(x,y)
          t.pendown()
          
def num(t,n):
          y=230
          mov(100,y,t)
          t.write("Tablero enemigo",False,"right", ("arial", 20, "bold italic"))
          y=y-30
          p=-150
          for x in range(n):
                    mov(p,y,t)
                    t.write("C"+str(x+1), False,"right", ("arial", 15, "bold italic"))
                    p+=50
          mov(-230,230,t)
          y=150
          p=-230
          for x in range(n):
                    mov(p,y,t)
                    t.write("F"+str(x+1), False,"right", ("arial", 15, "bold italic"))
                    y-=50
          
                    

def tablero():
          t=turtle.Turtle()
          t.speed(12)
          mov(-200,-200,t)
          for x in range(4):
                    t.fd(400)
                    t.left(90)
          for x in range(4):
                    t.fd(50)
                    t.left(90)
                    t.fd(400)
                    t.seth(0)
                    t.fd(50)
                    t.seth(270)
                    t.fd(400)
                    t.seth(0)
          for x in range(4):
                    t.seth(90)
                    t.fd(50)
                    t.left(90)
                    t.fd(400)
                    t.seth(90)
                    t.fd(50)
                    t.seth(0)
                    t.fd(400)
          num(t,8)
          
