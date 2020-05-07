#First Github Contribution
'''
This program perform the following conversions:
Temperature Conversions - Kelvin, Celsius, Fahrenheit
Distance Conversion     - Kilometre, Mile
Weight Conversion       - Kilogram, Pound
'''
import time #For loading effect

def loading():
    print('.', end='')
    time.sleep(0.5)
    print('.', end='')
    time.sleep(0.5)
    print('.')
    
def temperature_convert( temperature, input_type, output_type ):
    co = (input_type, output_type) #Input output combination.
    
    if   co == (1,2):
        return temperature - 273.15
    
    elif co == (1,3):
        celsius = temperature - 273.15
        return (9*celsius/5) + 32
    
    elif co == (2,1):
        return temperature + 273.15
    elif co == (2,3):
        return 9*temperature/5 + 32
    
    elif co == (3,1):
        celsius = (5/9)*(temperature-32)
        return celsius + 273.15
    elif co == (3,2):
        return (5/9)*(temperature-32)
    
    else:
        return "Invalid Input"
    

def distance_convert( distance, input_type ):
    
    if input_type == 1:
        return distance * 0.621371
    elif input_type == 2:
        return distance * 1.60934
    
    else:
        return "Invalid Input"


def mass_convert( mass, input_type ):
    
    if input_type == 1:
        return mass * 2.20462
    elif input_type == 2:
        return mass * 0.453592
    
    else:
        return "Invalid Input"

#Main:
loading()
print("Conversions!")

while( True ):
    
    loading()
    print("\nWhat should I convert?")
    print("1 - Temperature")
    print("2 - Distance")
    print("3 - Weight")
    print("0 - Exit")
    
    inp = int(input("Enter choice:"))
    if inp == 1:
        print("1 - Kelvin")
        print("2 - Celsius")
        print("3 - Fahrenheit")
        print("Enter input format along with the Temperature: (Example: 1 273.15)",end='')
        input_type, temperature = [ float(i) for i in input().split() ]
        print("Enter output format:",end='')
        output_type = int(input())
        answer = temperature_convert( temperature, int(input_type), output_type )
        loading()
        
        if type(answer) == 'int':
            print("Answer: ", answer )
        else:
            print(answer)
            
    elif inp == 2:
        print("1 - Kilometre")
        print("2 - Mile")
        
        print("Enter input format along with the Distance: (Example: 1 200)",end='')
        input_type, distance = [ float(i) for i in input().split() ]
      
        answer = distance_convert( distance, int(input_type) )
        loading()
        
        if type(answer) == 'int':
            print("Answer: ", answer )
        else:
            print(answer)
    
    elif inp == 3:
        print("1 - Kilogram")
        print("2 - Pound")
        
        print("Enter input format along with the Mass: (Example: 1 1000)",end='')
        input_type, mass = [ float(i) for i in input().split() ]
     
        answer = mass_convert( mass, int(input_type) )
        loading()
        
        if type(answer) == 'int':
            print("Answer: ", answer )
        else:
            print(answer)
            
    elif inp == 0:
        loading()
        print("Terminating Program!")
        break
    else:
        print("Invalid Input")
        
#End
