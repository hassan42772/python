# SIMPLE CALCULATOR
print("please enter first number :")
num1=int(input())
print("please enter operator :")
operator=input()
print("please enter second number :")
num2=int(input())
sum=num1+num2
diff=num1-num2
mul=num1*num2
dvd=num1/num2
if  operator == "+":
    print(sum)
elif operator == '-':
    print(diff)
elif operator == '*':
    print(mul)
elif operator == '/':
    print(dvd)  
else:
    pass