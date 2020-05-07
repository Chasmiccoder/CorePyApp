
# print("This file is edit by Kusheshwar Mandal")
#print("Whats up python!")
# importing calendar module
import calendar
import requests #imporing requests module to get the api url of currency

#address of api url currency
api_url_end='https://api.exchangeratesapi.io/latest?base=USD'
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
    try:
        return x / y
    except ZeroDivisionError:
        print("\nCannot divide by zero.\n")


def data_convertor(B):
    B = float(B)
    KB = float(1024)
    MB = float(KB ** 2) # 1,048,576
    GB = float(KB ** 3) # 1,073,741,824
    TB = float(KB ** 4) # ,099,511,627,7761
    if B < KB:
       return '\n{0:.5f} KB\n{1:.5f} Bytes\n{2:.5f} Bits'.format(B/KB,B,B*8)
    elif KB <= B < MB:
       return '\n{0:.5f} MB\n{1:.5f} KB\n{2:.5f} Bytes\n{3:.5f} Bits'.format(B/MB,B/KB,B,B*8)
    elif MB <= B < GB:
       return '\n{0:.5f} GB\n{1:.5f} MB\n{2:.5f} KB\n{3:.5f} Bytes\n{4:.5f} Bits'.format(B/GB,B/MB,B/KB,B,B*8)
    elif GB <= B < TB:
       return '\n{0:.5f} TB\n{1:.5f} GB\n{2:.5f} MB\n{3:.5f} KB\n{4:.5f} Bytes\n{5:.5f} Bits'.format(B/TB,B/GB,B/MB,B/KB,B,B*8)
    elif TB <= B:
       return '\n{0:.5f} TB\n{1:.5f} GB\n{2:.5f} MB\n{3:.5f} KB\n{4:.5f} Bytes\n{5:.5f} Bits'.format(B/TB,B/GB,B/MB,B/KB,B,B*8)

def currency_convertor(currency_from,currency_to,amount):
        rate=response.json()['rates'][currency_from]
        amount_in_USD=amount/rate
        result=amount_in_USD*(response.json()['rates'][currency_to])
        result=round(result,2)
        print('\n{0} {1} = {2}  {3}'.format(amount,base_currency,result,convert_to))

def distance_converter(m):
    print('\nMiles      : {0:.2 f}  mi'.format(m))
    yards = m * 1760
    print("Yards      : {0:.2f}  ya" .format(round(yards,2)))
    feet = m * 5280
    print("Feet       : {0:.2f}  ft" .format(round(feet,2)))
    inches=feet*12
    print('Inches     : {0:.2f} in'.format(round(inches,2)))
    k =round( m * 1.60934,2)
    
    print("Kilometers : {0:.2f} km" .format(k))
    meters = round(m * 1609.35,2)
    print("Meters     : {0:.2f} m" .format(round(meters,2)))
    centimeters = meters * 1000
    print("Centimeters: {0:.2f} cm" .format(round(centimeters,2)))
    milimeters = centimeters * 1000
    print("Milimeteres: {0:.2f} mm" .format(round(milimeters,2)))
    print('\n\tThank You! For using Distance converte !!')


print("\n")
print("We have two apps for you:")
print("1.Calculator")
print("2.Calendar")
print("3.Weight Converter")
print("4.Data Size Converter")
print("5.Currency Converter")
print("6.Temperature Converter")
print("7.Distance Converter")
app = input("Select one app from above(/1/2/3/4/5/6/7/8): ")


if app == '1':
    print("\nThanks for choosing calculator, \n please Select one operation from below:")
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

elif app=='2':
    # To take month and year input from the user
    yy = int(input("Enter year: "))
    mm = int(input("Enter month: "))

# display the calendar
    print("\n")
    print(calendar.month(yy, mm))

elif app=='3':
    print("\n \t  Welcome to Weight Converter \n \nplease,  Select number from below:")
    print("1 For kilogram to pound")
    print("2.for Pound to kilogram")
    c = input("Enter choice one(/1/2/) : ")
    if c =='1':
        kg=float(input('Enter the weight in KG:'))
        print("\n%.2f KG = %.2f LB.\n\n\t Thank You !" %(kg,kg*2.20462))
    elif c =='2':
        lb=float(input('Enter the weight in LB:'))
        print("\n%.2f LB = %.2f KG.\n\n\t Thank You !" %(lb,lb/2.20462))
    else:   
        print("\nInvalid Input")

elif app=='4':
    print("\n\t Welcome to Data Size Converter !\n \nplease,  Select number from below:")
    print("1. Enter Data in Bytes: ")
    print("2. Enter Data in KB:")
    print("3. Enter Data in MB:")
    print("4. Enter Data in GB:")
    print("5. Enter Data in TB:")
    KB = float(1024)
    c=input('choose one (1/2/3/4/5)  :')
    
    if c=='1':
         b = float(input("Enter data size in Bytes : "))
         print(data_convertor(b))
    elif c=='2':
         b = float(input("Enter data size in KB : "))
         print(data_convertor(b*KB))
    elif c=='3':
        b = float(input("Enter data size in MB : "))
        print(data_convertor(b*KB**2))
    elif c=='4':
        b = float(input("Enter data size in GB : "))
        print(data_convertor(b*KB**3))
    elif c=='5':
        b = float(input("Enter data size in TB : "))
        print(data_convertor(b*KB**4))
    else:
        print('\nInvalid Choice')

elif app=='5':
    print("\n \t  Welcome to Currency Converter ")
    response=requests.get(api_url_end)
    base_currency=input('Enter the base currency from '+str(response.json()['rates'].keys()) +':').upper()
    convert_to=input('Enter the result currency  '+str(response.json()['rates'].keys())+":").upper()
    amount_to_convert=int(input("Enter the amount to convert:  "))
    currency_convertor(base_currency,convert_to,amount_to_convert)


elif app == '6':
    print("\n\t Welcome to Temperature Converter !\n \nplease,  Select number from below:")
    print("1. For celsius to Farenheit: ")
    print("2. For Farenheit to celsius: ")
    c=input('choose one (/1/2/)  : ')
    if c=='1':
        celsius = float(input("Enter temperature in celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print('\n%.2f Celsius is equal to %0.2f Fahrenheit.\n\n\t Thank You !' %(celsius, fahrenheit))
    elif c=='2':
        fahrenheit = float(input("Enter temperature in fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print('\n%.2f  Fahrenheit is equal to  %0.2f Celsius .\n\n\t Thank You !' %(fahrenheit, celsius))
    else:
        print("\nInvalid Input")


elif app =='7':
    print("\n\t Welcome to Distance Converter !\n \nplease,  Select number from below:")
    print("1=> for lenght in Miles : ")
    print("2=> for lenght in Kilometer:")
    print("3=> for lenght in Feet:")
     
    l=input('Please enter one (/1/2/3/)  :')
    
    if l=='1':
        mil=float(input('Enter lenght in Miles : '))
        distance_converter(mil)
    elif l=='2':
        kil=float(input('Enter lenght in kilometer : '))
        distance_converter(kil*0.62137)
    elif l=='3':
        feet=float(input("Enter lenth in feet : "))
        distance_converter(feet/5280)
    else:
        print('\nInvalid Input')

else:
    print(" \n Invalid Input")