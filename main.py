import turtle

class box(turtle.Turtle):
  
  def __init__(self,x,y,w,h):
      turtle.Turtle.__init__(self)
      self.shape("square")
      self.color("white")
      self.penup()
      self.goto(x,y)
      self.shapesize(w,h)
   
  def up(self):
    self.sety(self.ycor() + (self.ycor() < 220) * 40)
    
  def dw(self):
    self.sety(self.ycor() - (self.ycor() > -220) * 40)

  def draw(self):
    self.write("0       0".format(self.pts, self.ptsPc),
               font=("Arial", 40, "normal"), align = "center")


class Score(box):
  def __init__(self,x,y,w,h):
    box.__init__(self,x,y,w,h)
    self.goto(x,y)
    self.pts = 0
    self.ptsPc = 0
    self.hideturtle()
    self.draw()
  

class Bol(box):
  def __init__(self,x,y,w,h):
      box.__init__(self, x, y, w, h)
      self.pcy = 0
      self.bx = 0
      self.by = 0
      self.vx = 0
      self.vy = 0

  def update(self):
    self.bx += self.vx
    self.by += self.vy
    bol.goto(self.bx,self.by)
    p2.goto(p2.xcor(), self.pcy)
    if self.bx >= p2.xcor() - 30:
      self.vx *= -1
    if self.bx <= p1.xcor() + 30 and self.by < p1.ycor() + 100 and self.by> p1.ycor() - 100:
      self.vx *= -1
    elif self.bx < p1.xcor():
      self.vx *= -1
      self.bx = 0
      score.pts +=1
      score.clear()
      score.draw()
      
    if self.by >= 280 or self.by <= - 280:
      self.vy *= -1
    if self.bx > 20:
      if p2.ycor() < self.by and self.pcy < 220:
        self.pcy += 1
      if p2.ycor() > self.by and self.pcy > -220:
        self.pcy -= 1
 





#criando a janela, dando título, setando a cor preta com 800 de largura e 600 de altura

#win = start()
class inicio():
  ini = turtle.Screen()
  ini.title('-- Ping Pong XD --')
  ini.bgcolor("purple")
  ini.setup(width = 800,height = 600)
  ini.tracer(0)
  ini = start()

p1 = box(-350,0,8,1)
p2 = box(350,1,8,1)
bol = Bol(0 ,0 ,2, 2)
score = Score(0,230,10,10)

class star():
  win = turtle.Screen()
  win.title('-- BOA SORTE ! --')
  win.bgcolor("black")
  win.setup(width = 800,height = 600)
  win.tracer(0)

  #verificando teclas apertadas
  win.listen()
  win.onkeypress(p1.up, "Up")
  win.onkeypress(p1.dw, "Down")

go = inicio()

while True:
  #win.update()
  #bol.update()
  inicio.update()
  