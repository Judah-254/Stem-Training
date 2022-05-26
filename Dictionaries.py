#Dictionaries in python
mydict={
    "Book":"Dynamics",
    "publisher":"Longhorn",
    "Year":2001
}
#Accessing items
x=mydict ["Year"]
print(x)

#Accesing using get()
y=mydict["Year"]
print (y)

#All keys
x=mydict.keys()
print (x)

#All values
x=mydict.values()
print(x)

#Printing all items in a dictionary
x=mydict.items()
print(x)

#Checking 
if "publisher" in mydict:
    print("publisher is one of the keys")
    
#Dictionaries can hold diffeernt data types
mydict={
    "Book":"Dynamics",
    "publisher":"Longhorn",
    "Year":2001,
    "Authors":["John","Mike","Judah"]
}
x=mydict.values()
print(x)
