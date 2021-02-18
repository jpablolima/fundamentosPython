import turtle

# vegeta = turtle.Turtle()
# gohan = turtle.Turtle()

# def square(t, length):
#     for i in range(10):
#         t.fd(100)
#         t.fd(length)
#         t.lt(90)
# square(vegeta, 100)
# square(gohan)


gothen = turtle.Turtle()

def polygon(t, n, length):
     angle = 360 / n
     for i in range(n):
         t.fd(length)
         t.lt(angle)
polygon(gothen, 10 ,70)