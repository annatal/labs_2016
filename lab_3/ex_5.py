import turtle

for i in range(10 ,200, 20):
    turtle.pendown()
    turtle.shape('turtle')
    turtle.forward(i)
    turtle.left(90)
    turtle.forward(i)
    turtle.left(90)
    turtle.forward(i)
    turtle.left(90)
    turtle.forward(i)
    turtle.penup()
    turtle.forward(10)
    turtle.left(90)
    turtle.backward(10)
  
