##def max_number_num1_num2():
##    num1 = int(input("enter a number "))
##    num2 = int(input("enter a number "))
##    if num1<num2:
##               print(num1,"is the smallest number")
##    elif num1 == num2:
##        print(num1, "and",num2,"are same")
##    else:
##        print(num2,"is the smallest number")
##        
##max_number_num1_num2()
##
##
##def inter_number_5_15(num1):
##    if num1>=5 and num1<=15:
##        print(num1,"is in the range of 5-15")
##
##    else:
##        print(num1,"is outside of the range")
##
##
##num1 = int(input("enter a number "))
##inter_number_5_15(num1)
##
##
##def product():
##    num1 = int(input("enter a number "))
##    num2 = int(input("enter a number "))
##    add = num1*num2
##    print(add,"Is the product")
##
##product()


##def print_seconds_per_day():
##    minutes = int(input("enter a number "))
##    seconds = minutes * 60
##    print(seconds)
##
##print_seconds_per_day()



##def a_tri():
##    base = int(input("enter a number "))
##    height = int(input("enter a number "))
##    area = ((base*height)/2)
####    return area
##
##def a_sq():
##    width = int(input("enter a number "))
##    height = int(input("enter a number "))
##    areab = ((width*height))
##    return areab
##
####choice = input("enter y for square and n for triangle(y/n)")
##if choice == 'y':
##    sq=a_sq()
##    print(sq)
##else:
##    tri=a_tri()
##    print(tri)




##def print_seconds_per_hour():
##
##    hours = int(input("enter a number "))
##    minutes = hours * 60
##    seconds = minutes * 60
##    print(seconds)
##
##print_seconds_per_hour()


def p_sq():
    width = int(input("enter a number "))
    height = int(input("enter a number "))
    peri = ((width*2) + (height*2))
    return peri

def a_sq():
    width = int(input("enter a number "))
    height = int(input("enter a number "))
    areab = ((width*height))
    return areab


use = 'y'
while use == 'y':
    choice = input("enter a for area and p for perimeter(a/p)")
    if choice == 'a':
        sq=a_sq()
        print(sq)
    elif choice  =='p':
        sq2 = p_sq()
        print(sq2)
    else:
        print("incorect input recieved")

    use = input("enter y to run again and n to stop(y/n)")
