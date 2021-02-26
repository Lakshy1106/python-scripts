#-------------IMPORTING FUNCTIONS FROM LIBRARY-----------------------------------
import math
import numpy

#------------FUNCTION DECLARATION------------------------------------------------
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

#-------------------USER INTERFACE SECTION------------------------------------------

while 1:
    operation = input('''
Select your operation
1. Factorial
2. Addition
3. Subtract
4. Multiply
5. Division
6. Square Root
7. Power
8. Natural Logarithm
9. Logarithm of any Base
10.Cartesian to Polar
11.Polar to Cartesian
12.Degree to Radian conversion
13.Radian to Degree conversion
14.Celsius to Farhenheit
15.Farhenheit to Celsius
16.End calculator
''')
    if operation == "1":
        factorial()
    if  operation == '2':
        addition()
    if  operation == '3':
        subtract()
    if  operation == '4':
        multiply()
    if  operation == '5':
        division()
    if  operation == '6':
        sqroot()
    if  operation == '7':
        power()
    if  operation == '8':
        nlog()
    if operation == '9':
        log()
    if operation == '10':
        Cartesian2Polar()
    if operation == '11':
        Polar2Cartesian()
    if operation == '12':
        x = int(input("The angle in degrees - "))
        deg2rad(x)
    if operation == '13':
        x = int(input("The angle in radians - "))
        rad2deg(x)
    if operation == '14':
        Celsius2Farhenheit()
    if operation == '15':
        Farhenheit2Celsius()
    if operation == '16':
        break
    print('\n--------------OPERATION COMPLETED--------------')

#------------------------END SECTION--------------------------------------------
print ("-----------------------------END OF PROGRAM--------------------------")
