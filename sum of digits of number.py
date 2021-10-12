
def sum_of_Digit(num):
    total=0
    while num!=0:
        temp=num%10
        total+=temp
        num=num//10
    print("Total :",total)

sum_of_Digit(123)