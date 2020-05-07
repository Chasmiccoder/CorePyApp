def menu():
    print("\n")
    print("We have three apps for you:")
    print("1.Kilo bytes convert into Mega bytes")
    print("2.Kilo bytes convert into Mega bytes")
    print("3.Mega bytes convert into Gega bytes")
    print("4.Exit")
    app =int(input("\nEnter a Choice :"))
    return app

def kb_mb(x):
    return ((x)*0.001)
def kb_gb(x):
    return ((x)*0.000001)
def mb_gb(x):
    return ((x)*0.001)

def main():
    choose = menu()
    if choose == 1 :
        num = int(input("Enter the digit you want to convert to Mega bytes :"))
        print (num,  "KB","=" , kb_mb(num) ,"MB")
    
    elif choose == 2:
        num = int(input("Enter the digit you want to convert to Gega bytes :"))
        print (num, "KB", "=", kb_gb(num), "GB")
    
    elif choose == 3:
        num = int(input("Enter the Mega bytes you want to convert to Gega bytes :"))
#       print (num, "MB", "=", '{r:1.2f}'.format(r=(mb_gb(num)), "GB")
        print (num, 'MB', "=", mb_gb(num), "GB")
    
    elif choose == 4:
        exit()
    else:
        print ("\nInvalied Entry")
        print ("Try Next Time")       
main()