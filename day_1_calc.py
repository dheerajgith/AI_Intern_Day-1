def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a*b
def div(a,b):
    if b==0:
        return "Error:denom is 0 "
    return a/b
def mod(a,b):
    if b==0:
        return "Error:denom is 0 "
    return a%b
def exp(a,b):
    return a**b

while True:
    print("Choose Operation:\n" 
    "1.Add or 2.Subtract or 3.Multiply or 4.Divide or 5.Modulus or 6.Exponent or 7.Exit")
    ch=input("Enter choice(1/2/3/4/5/6/7): ")
    if ch not in ('1','2','3','4','5','6','7'):
        print("Invalid Input")
        continue
    if ch=='7':
        print("Exiting..")
        break
    else:
        a=float(input("enter 1st num "))
        b=float(input("enter 2nd num "))
        if ch=='1':
            print(add(a,b))
        elif ch=='2':
            print(sub(a,b))
        elif ch=='3':
            print(mul(a,b))
        elif ch=='4':
            print(div(a,b))
        elif ch=='5':
            print(mod(a,b))
        elif ch=='6':
            print(exp(a,b))
