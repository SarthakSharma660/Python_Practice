import os
import art
def sum1(n1,n2):
    return n1+n2
def substract(n1,n2):
    if n1>n2:
        return n1-n2
    else:
        n2-n1
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    if n2==0:
        return "invalid can not be divided by 0"
    else:
        return n1/n2
operator={
    "+":sum1,
    "-":substract,
    "*": multiply,
    "/": divide
}
def calc():
    print(art.logo)
    f_number=float(input("What's the first number?:"))
    more="yes"
    while more =="yes":
        for symbol in operator:
            print (symbol)
        operator_input=input("Pick an operation: ")
        s_number=float(input("What's the next number?:"))
        function=operator[operator_input]
        result=function(f_number,s_number)
        print(f"result is :{result}")
        more =input(f"'yes' to continue calculating with {result}, or type 'no' to start a new calculation\n").lower()
        if more=="yes":
            f_number=result
        else:
            os.system("clear")
            calc()
        
calc()        

            