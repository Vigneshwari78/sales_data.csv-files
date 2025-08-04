operator=input("enter the operator(+ - * / ):")
num1=float(input("enter the 1st value:"))
num2=float(input("enter the 2nd value:"))
if operator=="+":
    result=num1+num
    print(result)
elif operator=="-":
    result=num1-num2
    print(result)
elif operator=="*":
    result=num1*num2
    print(result)
elif operator=="/":
    result=num1/num2
    print(result)
else:
    print(f"{operator} is not a valid operator")