# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
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
   return x / y

print("\n")
print("We have two apps for you:")
print("1.Calculator")
print("2.Calendar")
app = input("Select one app from above\n (1 for Calculator 2 for calender): ")
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
else:
    # To take month and year input from the user
    yy = int(input("Enter year: "))
    mm = int(input("Enter month: "))

# display the calendar
    print("\n")
    print(calendar.month(yy, mm))
