def menu():
    print("\n")
    print("We have two apps for you:")
    print("1.Celsius to Fahrenheit")
    print("2.Fahrenheit to Celsius")
    print("3.Exit")
    pick =int(input("\nEnter a Choice :"))
    return pick

def fah_cel(f):
    """
    Accepts degrees Fahrenheit (fahrenhit argument)
    Returns degrees Celsius
    """
    c =((f - 32) *(5/9))
    return int(c)

def cel_fah(c):
    """
    Accepts degrees Celsius (celsius argument)
    Returns degrees fahrenheit
    """
    f = (c * (9/5))+ 32
    return int(f) 
    
def main_1():
    choice = menu()
    if choice == 1:
            # convert C to F
        print("Thanks for choosing Celsius to Fahrenheit.")
        c = int(input('Enter the Celsius Degree :'))
        print (str(c) + "C =" + str(cel_fah(c)) +"F")
        
    elif choice == 2:
            # Conver to Fahrenheit
        print("Thanks for choosing Fahrenheit to Celsius.")    
        f=int(input('Enter the Fahrenheit Degree :'))
        print(str(f) + "F =" + str(fah_cel(f)) + "C")
            
    elif choice == 3:
        exit()
    
    else : 
        print ("Invalid Entry")
        print("Try Again Next Time")

# synatax to laad app
main_1()         