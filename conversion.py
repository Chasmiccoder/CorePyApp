# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# -*- coding: utf-8 -*-
"""
Add a new app called converter to the existing tool.
This new app should offer two choices- temperature converter and distance converter.
Currently this tool offers two apps- Calculator and calendar. I have attached the existing code. You will be writing your own code to add new app.
BONUS POINTS 1 - add weight converter
BONUS POINTS 2 - add data size converter
BONUS POINTS 3 - add currency converter
BONUS POINTS 4 - add temperature converter
BONUS POINTS 5 - add date converter
"""

#print("Whats up python!")
# importing calendar module
import calendar
# Program make a simple calculator
# This function adds two numbers 
def add(x, y):
   return x + y
# This function subtracts two numbers 
def subtract(x, y):
   return x - y
# This function multiplies two numbers
def multiply(x, y):
   return x * y
# This function divides two numbers
def divide(x, y):
   return x / y if y else 0

print("\n")
print("We have five apps for you:")
print("1. Calculator")
print("2. Calendar")
print("3. Weight convert")
print("4. Temperature convert")
print("5. Distance convert")
app = input("Select one app from above\n (1 for Calculator 2 for calender 3 Weight convert emperature convert 4 for temperature converter and 5 for Distance converter:) ")
if app == '1':
    print("Thanks for choosing calculator, \n please Select one operation from below:")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    choice = input("Enter choice(1/2/3/4): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if choice == '1':
        print(num1,"+",num2,"=", add(num1,num2))
    elif choice == '2':
        print(num1,"-",num2,"=", subtract(num1,num2))
    elif choice == '3':
        print(num1,"*",num2,"=", multiply(num1,num2))
    elif choice == '4':
        print(num1,"/",num2,"=", divide(num1,num2))
    else:
        print("Invalid input")
elif app == '2':
    # To take month and year input from the user
    yy = int(input("Enter year: "))
    mm = int(input("Enter month: "))
# display the calendar
    print("\n")
    print(calendar.month(yy, mm))

elif app == '3':
    print("In what do you want to convert? 1.To pound 2. To KG")
    nos=input("Press either 1 or 2:")
    weight=float(input("Enter weight:"))
    if nos == '1':
        kg = weight * 2.2046
        print(weight, 'Kg=', kg, 'Pounds')
    else:
        pound = weight * 0.453592
        print(weight, 'Pound = ', pound, 'Kg')

elif app == '4':
    print("In what do you want to convert? 1.To Celsius 2. To Fahrenheit")
    no=input("Press either 1 or 2:")
    temp=float(input("Enter Temperature: "))
    if no == '1':
        celsius =(temp-32)*5.0/9.0
        print(temp, 'Fahrenheit =', celsius, 'Celsius')
    else:
        fah=9.0/5.9 * temp +32
        print(temp, 'Celsius = ', fah, 'F')

elif app == '5':
    print("In what do you want to convert? 1.To KM 2. To Miles")
    no=input("Press either 1 or 2:")
    dist=float(input("Enter Distance: "))
    if no == '1':
        km= dist*1.60934
        print(dist, 'miles =', km, 'KM')
    else:
        miles=dist*0.62137
        print(dist, 'Km = ', miles, 'Miles')

else:
    print('Please retry after reading instructions. Thank you.')