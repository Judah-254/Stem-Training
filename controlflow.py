#IF statements
x=0
if x>=1:
    print ("Hey im still there")
    x-=1
    print (x)
print ("Done")
# Else statements
x=10
if x==10:
    print (x)
else:
    print ("Not 10")
#Elif to create a grading  system
Grade = int(input("Write students score"))
if Grade >=80 and Grade<=100:
    print("Student got an A")
elif Grade >=70 and Grade <80:
    print ("Student got a B") 
elif Grade >=60 and Grade <70:
    print ("Student got a C")
elif Grade >50 and Grade <60:
    print ("Student got a D")
elif Grade >40 and Grade <50:
    print ("Student got a E")
else:
    Grade >30
    print("Below average")



