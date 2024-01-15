import turtle as t
t.bgcolor("black")
t.goto(0, 200)
a = 0
b = 0
t.tracer(100)
t.pencolor("green")
while True:
    t.forward(a)
    t.right(b)
    a = a+3
    b = b+1
    if b==210:
        break
    t.hideturtle()
t.mainloop()