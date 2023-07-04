num1=(int(input('enter first number\n')))
num2: int=(int(input('enter second number\n')))
num3=(int(input('to add press 1,to subtract press 2,to multiply press 3,to divide press 4, to find mod press 5, to take exponent press 6, to exit press 0\n')))
while num3 !=0:
    if num3==1:
        print(num1+num2)
        num3 = (int(input('to add press 1,to subtract press 2,to multiply press 3,to divide press 4, to find mod press 5, to take exponent press 6, to exit press 0\n')))

    elif num3==2:
        print(num1-num2)
        num3 = (int(input('to add press 1,to subtract press 2,to multiply press 3,to divide press 4, to find mod press 5, to take exponent press 6, to exit press 0\n')))

    elif num3 == 3:
        print(num1*num2)
        num3 = (int(input('to add press 1,to subtract press 2,to multiply press 3,to divide press 4, to find mod press 5, to take exponent press 6, to exit press 0\n')))

    elif num3 == 4:
        print(num1/num2)
        num3 = (int(input('to add press 1,to subtract press 2,to multiply press 3,to divide press 4, to find mod press 5, to take exponent press 6, to exit press 0\n')))

    elif num3 == 5:
        print(num1%num2)
        num3 = (int(input('to add press 1,to subtract press 2,to multiply press 3,to divide press 4, to find mod press 5, to take exponent press 6, to exit press 0\n')))

    elif num3 == 6:
        print(num1**num2)
        num3 = (int(input('to add press 1,to subtract press 2,to multiply press 3,to divide press 4, to find mod press 5, to take exponent press 6, to exit press 0\n')))

    elif num3==0:
        break
