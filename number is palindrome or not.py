num=123
temp=num
temp1=0

while temp!=0:
    temp1=temp1*10+temp%10
    temp=temp//10

if temp1==num:
    print("palindrom")
else:
    print("Not a palindrom")
