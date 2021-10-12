def count(string,char):
    temp=""
    for i in string:
        temp+=i
        if i==char:
            print(len(temp))

count("veera","a")