#for loops in python 
mangoes="Book"
for i in mangoes:
    print (i)
print("Done")

# for loops with lists
words=["1","DID","A"]
for word in words:
    print (word +"!" )
#Counting letters in a string
str="Helo guys welcome back to my class"
count=0
for x in str:
        if(x=='o'):
            count +=1
        print ("number of o's is:",x)
str="Helo guys welcome back to my class"
for x in str:
        if(x=='l'):
            continue
        else:
            print(x)





