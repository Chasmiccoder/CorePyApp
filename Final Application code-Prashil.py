## -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 11:14:39 2020

@author: My_Device
"""

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

def kgtopound(kgweight):
    pound  = (float(kgweight)*2.2046)
    return pound

def poundtokg(poundweight):
    kg  = (float(poundweight)/2.2046)
    return kg

def celtofah(celtemp):
    fahrenheit = (float(celtemp)*2.2046) + 32
    return fahrenheit

def fahtocel(fahtemp):
    celcius = (float(fahtemp)/2.2046) - 32
    return celcius

def INRTONPR(INRCurrency):
    NPR = (float(INRCurrency*1.60))
    return NPR

def USDTONPR(USDCurrency):
    Neplease_Currency = (float(USDCurrency*123.05))
    return Neplease_Currency

def kilobytestobits(kilobytesdata):
    bits = (float(kilobytesdata*8192))
    return bits

def kilobytestobytes(kilobites):
    bytes = (float(kilobytes*1024))
    return bytes

def feettoinch(feet):
    inch = (float(feet*12))
    return inch

def feettoyard(feet):
    yard = (float(feet/3))
    return yard

def feettomiles(feet):
    miles = (float(feet/5280.02))
    return miles

print("\n")
print("We have seven apps for you:")
print("1.Calculator")
print("2.Calendar")
print("3.Weight Converter")
print("4.temperature Converter")
print("5.Currency Converter")
print("6.Distance Converter")
print("7.Data Size converter")
app = input("Select one app from above\n 1 for Calculator \n 2 for calender \n 3 for weight converter \n 4 for Temperature converter \n 5 for currency Converter \n 6 for distance converter \n 7 for data size converter ")
if app == '1':
    try:
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
    except:
           print("Invalid Input")
elif app =='3':
    try:
        print("Thanks for choosing weight converter, \nplease select one operation from below: ")
        print("1. KG to Pound")
        print("2. Pound to KG")
        choice = input("Enter choice(1/2): ")
        if choice == '1':
            kg = float(input('Enter weight in kg(Enter numeric value, example 10) to Convert into pounds:'))
            print("pound =",round(kgtopound(kg),2))
        elif choice == '2':
            pound = float(input('Enter weight in pound(Enter numeric value, Example 15) to Convert into kg:'))
            print("kg =",round(poundtokg(pound),2))
        else:
             print("Invalid input")   
    except:
           print("Invalid Input")
elif app =='4':
    try:
        print("Thanks for choosing temperature converter, \nplease select one operation from below:")
        print("1. Celcius to Fahrenheit")
        print("2. Fahrenheit to Celcius")
        choice = input("Enter choice(1/2): ")
        if choice == '1':
            celcius = float(input('Enter temperature in celcius(Enter numeric value, example 10) to Convert into fahrenheit:'))
            print("fahrenheit =",round(celtofah(celcius),2))
        elif choice == '2':
            fahrenheit = float(input('Enter temperature in fahrenheit(Enter numeric value, Example 15) to Convert into celcius:'))
            print("celcius =",round(fahtocel(fahrenheit),2))
        else:
            print("Invalid input") 
    except:
           print("Invalid Input")
elif app =='5':
    try:
        print("Thanks for choosing currency converter, \n please select one operation from below:")
        print("1. INR to NPR")
        print("2. USD to NPR")
        choice = input("Enter choice(1/2): ")
        if choice =='1':
            INR = float(input('Enter currency in INR to Convert into NPR,pls enter numeric value:'))
            print("NPR=", round(INRTONPR(INR),2))
        elif choice =='2':
            USDCurrency = float(input('Enter currency in USD to Convert into NPR, please enter numeric value:'))
            print("Neplease_Currency=", round(USDTONPR(USDCurrency),2))
        else:
             print("Invalid input")
    except:
           print("Invalid Input")        
elif app =='6':
   try: 
    print("Thanks for choosing distance converter")
    
    print("1. convert feet to inches")
    print("2. convert feet to yards")
    print("3. convert feet to miles")
    choice = input("Enter choice(1/2/3): ")
    d_ft = float(input("Input distance in feet, input should be numeric:\n please select one operation from below: "))
    if choice =='1':
        print("The distance in inches is ", round(feettoinch(d_ft),5))
    elif choice =='2':
        print("The distance in yards is ", round(feettoyard(d_ft),5))
    elif choice =='3':
        print("The distance in miles is ", round(feettomiles(d_ft),5))
    else:
        print("Invalid input") 
   except:
          print("Invalid Input")
elif app =='7':    
  try:
    print("Thanks for choosing data converter, \n please select one operation from below: ")
    print("1. convert kilobytes to bits")
    print("2. convert kilobytes to bytes")
    choice = input("Enter choice(1/2): ")
    if choice =='1':
        kilobytes = float(input("Input data in kilobytes, input should be numeric value to convert into bits: "))
        print("bits =",round(kilobytestobits(kilobytes),2))
    elif choice =='2':
         kilobytes = float(input("Input data in kilobytes, input should be numeric value to convert into bytes: "))
         print("bytes =",round(kilobytestobytes(kilobytes),2))  
  except:
          print("Invalid Input")
else:
 try:
    # To take month and year input from the user
    yy = int(input("Enter year: "))
    mm = int(input("Enter month: "))

# display the calendar4
    
    print("\n")
    print(calendar.month(yy, mm))
 except:
          print("Invalid Input")