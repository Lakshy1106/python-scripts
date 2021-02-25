import math
import numpy

def deg2rad(deg):
    rad = deg*(math.pi/180)
    return(rad)
def rad2deg(rad):
    deg = rad*57.2958
    return(deg)
def addition():
    x = float(input("Operand 1 :"))
    y = float(input ("Operand 2 :"))
    z = x+y
    print(x, "+", y, "=", z)
    return
def subtract():
    x = float(input("Operand 1 :"))
    y = float(input("Operand 2 :"))
    z = x-y
    print(x, "-", y, "=", z)
    return
def multiply():
    x = float(input("Operand 1 :"))
    y = float(input("Operand 2 :"))
    z = x*y
    print(x, "*", y, "=", z)
    return
def division():
    x = float(input("Operand 1 :"))
    y = float(input("Operand 2 :"))
    if y == 0:
        print(" The calculator cannot divide with 0")
        return 'NA'
    z = x/y
    print(x, "/", y, "=", z)
    return
def sqroot():
    x = float(input("Operand 1 :"))
    z = math.sqrt(x)
    print("Square root of ", x, "=", z)
    return
def power():
    x = float(input("Number :"))
    y = float(input("Power :"))
    z = x**y
    print(x, "raised to ", y, "=", z)
    return
def nlog():
    x = float(input("Operand 1 :"))
    z = math.log(x)
    print("Natural logarithm of ", x, "=", z)
    return
def log():
    x = float(input("Number :"))
    y = float(input("Base :"))
    z = math.log(x, y)
    print("Logarithm of", x, "in base", y, "=", z)
    return
def Polar2Cartesian():
    r = float(input("Enter radius : "))
    d = float(input("Enter theta in degrees: "))
    theta = d*math.pi/180
    x = r*math.cos(theta)
    y = r*math.sin(theta)
    print("x = {} and y= {}".format(x, y))
def Cartesian2Polar():
    x = float(input("What is the x coordinate?"))
    y = float(input("What is the y coordinate?"))
    r = math.sqrt(float(x**2)+float(y**2))
    theta = math.atan((y/x))
    theta = theta*57.2958
    print("Radius r = {} units, Angle theta = {} degrees".format(r, theta))
def Celsius2Farhenheit():
    C = float(input("Tempreature in Celsius :"))
    F= ((9/5)*C)+32
    print("The temperature in Farhenheit is {} ".format(F))
    return
def Farhenheit2Celsius():
    F = float(input("Temperature in farhenheit"))
    C = (F-32)*(5/9)
    print("The temperature in Celsius is {} ".format(C))
    return
def factorial():
    x = int(input("Operand 1 : "))
    z = math.factorial(x)
    print("The Factorial of {}! is {}".format(x,z))
    return
