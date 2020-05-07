#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 15:24:59 2020

@author: rahulawale
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
    if y==0:
        print ("Please use a number other than zero")
    else:
        return x / y

def celsius_converter(x):
    return ((x-32)/1.8)

def fahrenheit_converter(x):
    return ((x*1.8))+32

def miles_converter(x):
    return ((x * 0.621371))    
    
def km_converter(x):
    return((x / 0.621371))

def kg_converter(x):
    return((x/2.205))
    
def lbs_converter(x):
    return((x*2.205))

def kb_mb(x):
    return(x/(10**3))

def kb_gb(x):
    return((x/(10**6)))

def kb_tb(x):
    return((x/(10**9)))
    
def mb_kb(x):
    return(x*(10**3))
    
def mb_gb(x):
    return(x/(10**3))

def mb_tb(x):
    return(x/(10**6))

def gb_kb(x):
    return(x*(10**6))
    
def gb_mb(x):
    return(x*(10**3))

def gb_tb(x):
    return(x/(10**3))

def tb_gb(x):
    return(x*(10**3))

def tb_mb(x):
    return(x*(10**6))

def tb_kb(x):
    return(x*(10**9))

#importing forex module
from forex_python.converter import CurrencyRates
c= CurrencyRates()

def currency_converter(base_cur, dest_cur, amount):
    return(c.convert(base_cur, dest_cur, amount))
    
print("\n")
print("We have four apps for you:")
print("1.Calculator")
print("2.Calendar")
print("3.temperature_converter")
print("4.distance_converter")
print("5.weight_converter")
print("6.datasize_converter")
print("7.Currency Converter")
app = input("Select one app from above: \n(1) for Calculator\n(2) for calender\n(3) for temperature_converter\n(4) for distance_converter\n(5) for weight_converter\n(6) for data_converter\n(7) for currency_converter\n""\nEnter Here:")
if app == '1':
    print("Thanks for choosing calculator, \nplease Select one operation from below:")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    choice = input("Enter choice(1/2/3/4): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if choice =='1':
        print(num1,"+",num2,"=", add(num1,num2))
    elif choice == '2':
        print(num1,"-",num2,"=", subtract(num1,num2))
    elif choice == '3':
        print(num1,"*",num2,"=", multiply(num1,num2))
    elif choice == '4':
        print(num1,"/",num2,"=", divide(num1,num2))
    else:
        print("Invalid input")
        
if app =='2':
    print("Thanks for choosing calendar, \nplease enter the year and month:")
    # To take month and year input from the user
    yy = int(input("Enter year(yyyy): "))
    mm = int(input("Enter month(mm): "))

# display the calendar
    print("\n")
    print(calendar.month(yy, mm))
    
if app =='3':
    print("Thanks for choosing temperature_converter, \n please Select one operation from below:")
    print("1.fahrenheit to celsius converter")
    print("2.celsius to fahrenheit converter")
    pick= input("Enter pick(1/2):")
    temperature=float((input("Enter Temperature:")))
    if pick =='1':
        print(temperature,"°F","=", celsius_converter(temperature),"°C")
    elif pick =='2':
        print(temperature,"°C","=", fahrenheit_converter(temperature),"°F")
    else:
        print("Invalid input")
if app=='4':
    print("Thanks for choosing distance_converter, \n please Select one operation from below:")
    print("1.miles to kilometers converter")
    print("2.kilometers to miles")
    pick= input("Enter pick(1/2):")
    distance=float((input("Enter Distance:")))
    if pick =='1':
        print(distance,"Miles","=", km_converter(distance),"Kilometers")
    elif pick =='2':
        print(distance,"Kilometers","=", miles_converter(distance),"Miles")
    else:
        print("Invalid input")
if app=='5':
    print("Thanks for choosing weight_converter, \n please Select one operation from below:")
    print("1.kg to lbs")
    print("2.lbs to kg")
    pick= input("Enter pick(1/2):")
    weight=float((input("Enter weight:")))
    if pick =='1':
        print(weight,"kg","=", lbs_converter(weight),"lbs")
    elif pick =='2':
        print(weight,"lbs","=", kg_converter(weight),"kg")
    else:
        print("Invalid input")

if app=='6':
    print("Thanks for choosing datasize_converter, \n4please select your input data type:")
    print("1.kb")
    print("2.mb")
    print("3.gb")
    print("4.tb")
    data_choice = input("Select your choice (1/2/3/4): ")
    if data_choice =='1':
        data = float(input("Enter the data size:"))
        
        print("you have selected kb as your data type.\n""\nPlease select one of the choices below:\n1 for kb to mb\n2 for kb to gb\n3 for kb to tb")
        convert1= input("Enter choice (1/2/3):")
        if convert1=='1':
            print(data,"kb","=",kb_mb(data),"mb")
        elif convert1=='2':
            print(data,"kb","=",kb_gb(data),"gb")
        elif convert1=='3':
            print(data,"kb","=",kb_tb(data),"tb")
        else:
            print("Invalid input")
            
            
    elif data_choice =='2':
        data = float(input("Enter the data size:"))
        
        print("you have selected mb as your data type.\n""\nPlease select one of the choices below:\n1 for mb to kb\n2 for mb to gb\n3 for mb to tb")
        convert2= input("Enter choice (1/2/3):")
        if convert2=='1':
            print(data,"mb","=",mb_kb(data),"kb")
        elif convert2=='2':
            print(data,"mb","=",mb_gb(data),"gb")
        elif convert2=='3':
            print(data,"mb","=",mb_tb(data),"tb")
        else:
            print("Invalid input")
            
            
    elif data_choice =='3':
        data = float(input("Enter the data size:"))
        
        print("you have selected gb as your data type.\n""\nPlease select one of the choices below:\n1 for gb to kb\n2 for gb to mb\n3 for gb to tb")
        convert3= input("Enter choice (1/2/3):")
        if convert3=='1':
            print(data,"gb","=",gb_kb(data),"kb")
        elif convert3=='2':
            print(data,"gb","=",gb_mb(data),"mb")
        elif convert3=='3':
            print(data,"gb","=",gb_tb(data),"tb")
        else:
            print("Invalid input")
            
            
    elif data_choice =='4':
        data = float(input("Enter the data size:"))
        
        print("you have selected tb as your data type.\n""\nPlease select one of the choices below:\n1 for tb to kb\n2 for tb to mb\n3 for tb to gb")
        convert4= input("Enter choice (1/2/3):")
        if convert4=='1':
            print(data,"tb","=",tb_kb(data),"kb")
        elif convert4=='2':
            print(data,"tb","=",tb_mb(data),"mb")
        elif convert4=='3':
            print(data,"tb","=",tb_gb(data),"gb")
        else:
            print("Invalid input")          
    else:
        print("Invalid input")

if app=='7':
    print("Thanks for choosing currency_converter, \nplease follow the next steps:")
    base_cur=input("Enter the currency you have in the following format(United States Dollar=USD):")
    dest_cur=input("Enter the currency you want in the following format(Indian Rupees=INR):")
    amount=float(input("Enter Total Amount:"))
    convert=currency_converter(base_cur, dest_cur, amount)
    print(amount,base_cur,"=",convert,dest_cur)


    