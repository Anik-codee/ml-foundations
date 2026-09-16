def celsius_to_fahrenheit(celsius):  #Converting celsius to fahrenheit
    return (celsius*9/5)+32
a=float(input("Enter the temperature in celsius: "))
print("Temperature in fahrenheit will be: ", celsius_to_fahrenheit(a)) 

def calculate_average(a, b, c): #Calculating average of three numbers
    return(a+b+c)/3
a=float(input("Enter the first number: "))
b=float(input("Enter the second number: "))
c=float(input("Enter the third number: "))
print("The average of the three numbers is: ", calculate_average(a,b,c))

def calculate_percentage(obtained, maximum): #Calculating percentage
    if maximum==0:
        return None
    return (obtained/maximum)*100
x=float(input("Enter the obtained marks: "))
y=float(input("Enter the total marks: "))
print("Percentage is: ", calculate_percentage(x,y))

def calculate_power(voltage, current): #Calculating power
    return voltage*current
x=float(input("Enter the Voltage: "))
y=float(input("Enter the value of Current: "))
print("Power will be: ", calculate_power(x,y))

def calculate_energy(power, time): #Calculating Energy
    return power*time
x=float(input("Enter the value of Power: "))
y=float(input("Enter the Time taken: "))
print("Energy will be: ", calculate_energy(x,y))
