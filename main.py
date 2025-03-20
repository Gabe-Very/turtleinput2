import turtle
import random

screen = turtle.Screen()
screen.screensize(500, 500)
t = turtle.Turtle()
t.speed(0)
screen.bgcolor('Black')

turtle.Turtle()
#menu
t.penup()
t.goto(0,200)
t.pendown()
t.pencolor('White')
t.write("Background Color",font=("Arial",30,"bold"),align="center")

t.penup()
t.goto(-75,150)
t.pendown()
t.pencolor('Tan')
t.write("1. Tan",font=("Arial",20,"bold"),align="left")

t.penup()
t.goto(-75,100)
t.pendown()
t.pencolor('Azure')
t.write("2. Azure",font=("Arial",20,"bold"),align="left")


t.penup()
t.goto(-75,50)
t.pendown()
t.pencolor('Aquamarine')
t.write("3. Aquamarine",font=("Arial",20,"bold"),align="left")

t.penup()
t.goto(-75,0)
t.pendown()
t.pencolor('Darkkhaki')
t.write("4. Darkkhaki",font=("Arial",20,"bold"),align="left")

t.penup()
t.goto(0,-150)
t.pendown()
t.pencolor('blue')
t.write("Choose a Color",font=("Arial",30,"bold"),align="Center")

choose = int(input("Choose a Color: "))
if choose == 1:
    screen.bgcolor("Tan")
elif choose == 2:
    screen.bgcolor("Azure")
elif choose == 3:
    screen.bgcolor("Aquamarine")
else:
    screen.bgcolor("Darkkhaki")
t.clear()
t.penup()
t.goto(0,0)
t.pendown()
t.pencolor('Black')
t.write("Enter Your Name",font=("Arial",30,"bold"),align="Center")

name= input("Enter Your Name: ")
t.clear()
# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter a another number: "))
# sum1 = num1+num2
#
# t.penup()
# t.goto(0,100)
# t.pendown()
# t.pencolor('Blue')
# t.write(name,font=("Arial",30,"bold"),align="center")
#
# t.penup()
# t.goto(-200,0)
# t.pendown()
# t.pencolor('Green')
# t.write(num1,font=("Arial",30,"bold"),align="center")
#
# t.penup()
# t.goto(-100,0)
# t.pendown()
# t.pencolor('Red')
# t.write("+",font=("Arial",30,"bold"),align="center")
#
# t.penup()
# t.goto(0,0)
# t.pendown()
# t.pencolor('Hot Pink')
# t.write(num2,font=("Arial",30,"bold"),align="center")
#
# t.penup()
# t.goto(100,0)
# t.pendown()
# t.pencolor('Red')
# t.write("=",font=("Arial",30,"bold"),align="center")
#
# t.penup()
# t.goto(200,0)
# t.pendown()
# t.pencolor('Purple')
# t.write(sum1,font=("Arial",30,"bold"),align="center")
operation = random.randint(1,4)
if  operation == 1:
    symbol = "+"
    # add
    num1= random.randint(-100,100)
    num2= random.randint(-100,100)

    solution = num1 + num2

elif operation == 2:
    symbol = "-"
    # subtraction
    num1 = random.randint(-100, 100)
    num2 = random.randint(-100, 100)

    solution = num1 - num2

elif    operation == 3:
    symbol = "*"
    #multiply
    num1 = random.randint(-10, 10)
    num2 = random.randint(-10, 10)

    solution = num1 * num2

elif    operation == 4:
        symbol = "/"
        # division
        num1 = random.randint(-10, 10)
        num2 = random.randint(1, 10)
        sign = random.randint(1, 2)

        if sign == 2:
         num2 = -1+num2

        solution = num1 / num2

t.penup()
t.goto(0,100)
t.pendown()
t.pencolor('blue')
t.write(name,font=("Arial",30,"bold"),align="center")

t.penup()
t.goto(-200,0)
t.pendown()
t.pencolor('green')
t.write(num1,font=("Arial",30,"bold"),align="center")

t.penup()
t.goto(0,0)
t.pendown()
t.pencolor('pink')
t.write(num2,font=("Arial",30,"bold"),align="center")

t.penup()
t.goto(-100,0)
t.pendown()
t.pencolor('blue')
t.write(symbol,font=("Arial",30,"bold"),align="center")

t.penup()
t.goto(100,0)
t.pendown()
t.pencolor('red')
t.write("=",font=("Arial",30,"bold"),align="center")

ans  = float(input("Please enter your answer: "))

t.penup()
t.goto(200,0)
t.pendown()
t.pencolor('red')
t.write(solution,font=("Arial",30,"bold"),align="center")


t.penup()
t.goto(0,-100)
t.pendown()
t.pencolor('black')
t.write("Your answer was: "+str(ans),font=("Arial",30,"bold"),align="center")


if ans == solution:

    screen.bgcolor('DodgerBlue')

    t.penup()
    t.goto(0,-50)
    t.pendown()
    t.pencolor('Green')
    t.write("CORRECT!",font=("Arial",30,"bold"),align="center")

else:
        screen.bgcolor('Darkorange')

        t.penup()
        t.goto(0, -50)
        t.pendown()
        t.pencolor('Red')
        t.write("INCORRECT!", font=("Arial", 30, "bold"), align="center")












#This is the last line of code
turtle.done()