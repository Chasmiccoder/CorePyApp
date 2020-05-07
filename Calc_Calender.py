#print("Whats up python!")
# importing calendar module
import calendar
# Program make a simple calculator
# This function adds two numbers 

def menu():
    print("\n")
    print("We have two apps for you:")
    print("1.Calculator")
    print("2.Calender")
    print("3.Exit")
    app =int(input("\nEnter a Choice :"))
    return app



#app = input("Select one app from above\n (1 for Calculator 2 for calender): ")

def add(x, y):
   return (x + y)
# This function subtracts two numbers 

def subtract(x, y):
   return (x - y)
# This function multiplies two numbers

def multiply(x, y):
   return (x * y)
# This function divides two numbers

def divide(x, y):
   return (x / y)

def main_1():
    choose =menu()
    if choose == 1:
        print("Thanks for choosing calculator, \n please Select one operation from below:")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")
    
        choice = int(input("Enter choice(1/2/3/4): "))
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == 1:
            print(num1,"+",num2,"=", add(num1,num2))
        elif choice == 2:
            print(num1,"-",num2,"=", subtract(num1,num2))
        elif choice == 3:
            print(num1,"*",num2,"=", multiply(num1,num2))
        elif choice == 4:
            print(num1,"/",num2,"=", divide(num1,num2))
        else:
            print("Invalid input")
    
    
    elif choose ==2:
        # To take month and year input from the user
        yy = int(input("Enter year: "))
        mm = int(input("Enter month: "))

    # display the calendar
        print("\n")
        print(calendar.month(yy, mm))

    elif choose ==3: 
        exit()
    else :
        print ('Invalied Entry')  

main_1()

