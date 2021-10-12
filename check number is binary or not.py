num=101010
while num!=0:
    temp=num%10
    if temp!=0 and temp!=1:
        print("Number is not binary")
        break
    
    num=num//10
    if num==0:
        print("Number is binary")
        break
    
    