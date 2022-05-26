#Try,except in python to catch errors
try:
    div=10/0
    value=int(input("Enter a number:"))
    print(value)
except ValueError:
    print("Invalid ")
except ZeroDivisionError:
    print("Divided by zero")
    
