print ("Hey what's your first number")
a=0
while a<=10:
    a = int(input("Enter your first number"))
    print ("number must be greater than 10")
    if a>10:
        continue   
b=0
while b<=15:
    b = int(input("Enter your second number")) 
    print ("number must be greater than 15")
    if b>15:
        continue   
else:
    sum=(a+b)
    mult=(a*b)
    sub=(a-b)
print ("Printing answers from values")
print ("mult is:",mult)
print ("sum is",sum)
print ("Sub is",sub)

    





