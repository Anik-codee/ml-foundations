temp=[24,36,42,15] #Find average of temperature 
total=sum(temp)
avg=total/len(temp)
print("Average of temperature is: ", avg)

temp=[24,36,42,15,66,75] #Record temperature above a certain threshold
readings=[]
threshold=float(input("Enter a threshold temperature: "))
for i in temp:
    if i>threshold:
        readings.append(i)
print("Reading above the threshold is: \n",readings)
print("Count of the reading above the threshold is: \n",len(readings))

temp=[24,36,42,15,66,75] #New list containing only abnormal readings
abnormal_reading=[]
abnormal_temp=float(input("Enter temperature above which reading would be abnormal: "))
for i in temp:
    if i>abnormal_temp:
        abnormal_reading.append(i)
print("Original readings of temperature: \n",temp)
print("Abnormal readings of temperature: \n",abnormal_reading)

temp=[15,23,24,36,42,66,66,75,75] #Remove duplicate readings
temp=list(dict.fromkeys(temp))
print("List with removed duplicate elements: ", temp)

my_dict={} #Storing machine names and temperatures in a dictionary
entries=int(input("How many entries do you want to put: "))
for i in range(entries):
    key=input("Enter machine name: ")
    value=float(input("Enter temperature: "))
    my_dict[key]=value
print("Final collection of machines with temperature is: \n", my_dict)

my_dict = {                        #Finding machine with highest temp
    "Machine A": 15,
    "Machine B": 23,
    "Machine C": 24,
    "Machine D": 36,
    "Machine E": 42,
    "Machine F": 66
}
max_value=max(my_dict.values())
max_key=max(my_dict, key=my_dict.get)
print(f"The machine with maximum temperature is {max_key}, with maximum temperature {max_value}.")


words = ["motor", "pump", "motor", "fan", "pump", "motor"] #Finding frequency of item in list
frequency={}
for item in words:
    frequency[item]=frequency.get(item,0)+1
print(frequency)

