##def print_seconds_per_day():
##    hours = 24
##    minutes = hours * 60
##    seconds = minutes * 60
##    print(seconds)
##
##print_seconds_per_day()
##
##
##def print_seconds_per_day(days):
##    hours = days * 24
##    minutes = hours * 60
##    seconds = minutes * 60
##    print(seconds)
##
##day = int(input("enter a number"))
##print_seconds_per_day(day)
##
##
##def convert_days_to_seconds(days):
##    hours = days *24
##    minutes = hours * 60
##    seconds = minutes * 60
##    return seconds
##
##
##total_seconds = convert_days_to_seconds(7)#The return value is stored in the variable
##total_seconds
##milliseconds = total_seconds * 1000
##print(milliseconds)
##print("to make a funmction/ use def then the name of the function bracket on off and semicolon ")
##def print_seconds_per_day():
##    hours = int(input("enterw a number"))
##    minutes = hours* 60
##    seconds = minutes* 60
##    print(seconds)
##
##print_seconds_per_day()
##
##print("name needs nto have def in front and () in back and semicolon and name needs to be related to the topic of the function")
##def max_number_num1_num2():
##    num1 = int(input("enter a number "))
##    num2 = int(input("enter a number "))
##    if num1>num2:
##               print(num1,"is the biggest number")
##    elif num1 == num2:
##        print(num1, "and",num2,"are same")
##    else:
##        print(num2,"is the biggest number")
##        
##max_number_num1_num2()


##def inter_number_2_10(num1):
##    if num1>=2 and num1<=10:
##        print(num1,"is in the range of 2-10")
##
##    else:
##        print(num1,"is outside of the range")
##
##
##num1 = int(input("enter a number "))
##inter_number_2_10(num1)



##def add_sub():
##    num1 = int(input("enter a number "))
##    num2 = int(input("enter a number "))
##    add = num1+num2
##    print(add,"this is the numbers added")
##    if num1>num2:
##        sub = num1-num2
##        print(sub,"these are the results subtracted")
##
##    
##add_sub()


##def showemployee():
##    name = input("enter the name of the worker ")
##    sal = int(input("enter the workers salary "))
##    if sal == 5000: 
##        print("nice salary")
##    else:
##        sal == 5000
##        print("sal  == 5000")
##
##showemployee()


##    if sal == 5000:
##        print("good to go")
##
##    else:
##        print("You need to stop right here!")


def fizz_buzz():
    Fizz = int(input("enter a number "))
    Buzz = int(input("enter a number "))
    if Fizz %2==0:
        return Fizz

    elif Buzz %3==0:
        return Buzz

    else:
        return fizz_buzz


a=fizz_buzz()
print(a)


