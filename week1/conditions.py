def num_nature(a): #Check whether number is positive, negative, or zero
    if a>0:
        return "positive"
    elif a==0:
        return "zero"
    else:
        return "negative"
num=float(input("Enter the number to check: "))
print("Number is: ", num_nature(num))

def pass_or_fail(mark_obtained,chosen_mark): #To check whether student is passed or fail based on marks.
    if mark_obtained>=chosen_mark:
        return "passed"
    else:
        return "failed"
mark_obtained=float(input("Enter marks obtained: "))
chosen_mark=float(input("Enter minimum passing mark: "))
print("Student is ", pass_or_fail(mark_obtained,chosen_mark))

def machine_health(temp): #To evaluate health of machine based on temperature
    if temp<70:
        return "normal"
    elif temp<90:
        return "warning"
    else:
        return "critical"
temp=float(input("Enter the temperature of machine: "))
print("Machine status: ", machine_health(temp))

def greatest_num(a,b,c): #To check the greatest of given three number
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c
a=float(input("Enter a number a: "))
b=float(input("Enter a number b: "))
c=float(input("Enter a number c: "))
print("The greatest number is: ", greatest_num(a,b,c))

def student_grade(percentage): #To assign grade based on percentage
    if percentage>=75:
        return "A grade"
    elif percentage>=50:
        return "B grade"
    else:
        return "C grade"
percentage=float(input("Enter the percentage of the student: "))
print("Student has secured following grade: ", student_grade(percentage))

def find_largest(my_list): #Finding largest value in list.
    if len(my_list)==0:
        return "List is empty!"

    largest=my_list[0]
    for num in my_list:
        if num>largest:
            largest=num
    return largest
print("Largest number in the list is: ", find_largest([2,4,5,6,9]))