
from time import sleep
print('WELCOME TO BASIC CALCULATOR')
sleep(1)
print('for adition:- "+" \nfor subtraction:-"-" \nfor multiplication:-"*" \nfor division:-"div" ')
sleep(1)
choose=input('enter u r sign to proceed:')

if choose in ('+,-,*,div'):
            v1=float(input('enter u r first number:'))
            v2=float(input('enter u r secound number:'))

            if choose == '+':
                print(v1+v2)
            elif choose=='-':
                print(v1-v2)

            elif choose=='*':
                print(v1*v2)
            elif choose == 'div':
                print('D:-for int division')
                sleep(1)
                print('DIV:- for float division')
                sleep(1)
                print('%:- for modules')
                sleep(1)

                p=input('enter u r sign:')

                if p=='D':
                    print(v1//v2)
                elif p=='DIV':
                    print(v1/v2)
                elif p=='%':
                    print(v1%v2)
                else:
                    print('worng sign')
            else:
                print('worng sign')
else:
        print('u r input is worong')

print('THANKS FOR USING CALCULATOR')
sleep(1)
print('VISIT AGAIN')
