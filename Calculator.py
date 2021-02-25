#-------------IMPORTING FUNCTIONS FROM LIBRARY-----------------------------------

from functions import addition
from yfunctions import subtract
from functions import multiply
from functions import division
from functions import sqroot
from functions import power
from functions import nlog
from functions import log
from functions import deg2rad
from functions import rad2deg
from functions import Cartesian2Polar
from functions import Polar2Cartesian
from functions import Celsius2Farhenheit
from functions import Farhenheit2Celsius
from functions import factorial

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
