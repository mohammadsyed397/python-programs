import sys

def add(num1,num2):
    add = num1+num2
    return add
def sub(num1,num2):
    sub = num1-num2
    return sub
def mul(num1, num2):
    mul = num1*num2
    return mul
def division(num1, num2):
     division = num1/num2
     return division
def floatdivision(num1, num2):
    floatdivision = num1//num2
    return floatdivision
def reminder(num1, num2):
    reminder = num1%num2
    return reminder
    
num1 = int(sys.argv[1])
operation = sys.argv[2]
num2 = int(sys.argv[3])
if operation == "+":
    output = add(num1, num2)
    print(output)
if operation == "-":
    output = sub(num1-num2)
    print(output)
if operation == "*":
    output = mul(num1, num2)
    print(output)
if operation == "/":
   output = division(num1, num2)
   print(output)
if operation == "//":
   output = floatdivision(num1, num2)
   print(output)
if operation == "%":
    output = reminder(num1, num2)
    print(output)


