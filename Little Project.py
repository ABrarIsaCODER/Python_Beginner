
use = 'yes'
while use == 'yes':
    ui = int(input("enter a number 1-100 "))
    for i in  range(1,101):
        if ui%i == 0:
             print(ui,"Is divisible by",i)
    use = input("Ans y to stop con tinung and n to continue (yes/no)")


