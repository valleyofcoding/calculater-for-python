def ADITTION(firstNumber,secondNumber):
    return firstNumber+secondNumber
def SUBTRACTION(firstNumber,secondNumber):
    return firstNumber-secondNumber
def MULTIPLICATION(firstNumber,secondNumber):
    return firstNumber*secondNumber
def DIVISION(firstNumber,secondNumber):
    return firstNumber/secondNumber
firstNumber=float(input("Enter the first number: "))
operator=(input("Enter an operator: "))
secondNumber=float(input("Enter the second number: "))
if operator=="+":
    print(firstNumber,"+",secondNumber,"=",ADITTION(firstNumber,secondNumber))
elif operator=="-":
    print(firstNumber,"-",secondNumber,"=",SUBTRACTION(firstNumber,secondNumber))
elif operator=="*":
    print(firstNumber,"*",secondNumber,"=",MULTIPLICATION(firstNumber,secondNumber))
el15if operator=="/":
    print(firstNumber,"/",secondNumber,"=",DIVISION(firstNumber,secondNumber))
else:
    print("Error! operator is not correct")