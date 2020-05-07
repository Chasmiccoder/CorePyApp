def menu():
    print("\n")
    print("We have two apps for you:")
    print("1.Km Convert into Miles")
    print("2.Miles convert into Km")
    print("3.Exit")
    app =int(input("\nEnter a Choice :"))
    return app

def km(x): # Km into Miles
    return ((x)*0.609)

def ml(x): # Miles into Km
    return ((x)*1.609)

def main():
    choose = menu()
    if choose == 1 :
        num = int(input("Enter the digit you want to convert to Miles :"))
        print (num,  "Km","=" , km(num) ,"Miles")
    
    elif choose == 2:
        num = int(input("Enter the digit you want to convert to Km :"))
        print (num, "Miles", "=", ml(num), "Km")
    
    elif choose == 3:
        exit()
    
    else :
        print ("\nInvalied Entry")
        print ("Try Next Time")

# synatax to load app
main()