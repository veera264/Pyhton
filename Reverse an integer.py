

def reverse_number(num):
    rev_number=0
    while(num!=0):
        rev_number=rev_number*10+num%10
        num=num//10
    print("After Reverse Number:",rev_number,end="")

num=123
print("Before reverse Number:",num)
reverse_number(num)
