def menu():
    print("\n")
    print("We have two apps for you:")
    print("1.Poud convert into Kg")
    print("2.Kg convert into Pound")
    print("3.Exit")
    app =int(input("\nEnter a Choice :"))
    return app

def pd(x):
    return ((x)*0.453592)
def kg(x):
    return ((x)*2.20462)

def main():
    choose = menu()
    if choose == 1 :
        num = int(input("Enter the digit you want to convert to Kg :"))
        print (num,  "Pound","=" , pd(num) ,"Kg")
    
    elif choose == 2:
        num = int(input("Enter the digit you want to convert to Pound :"))
        print (num, "Kg", "=", kg(num), "Pound")
    
    elif choose == 3:
        exit()
    
    else :
        print ("\nInvalied Entry")
        print ("Try Next Time")
main()