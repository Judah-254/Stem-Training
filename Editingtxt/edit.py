#opening and editting files in python
role_file =open("roles.txt","r")
print(role_file.readline())

#Close file
role_file.close()

#write
role_file =open("roles.txt","a")
role_file.write("I love mee")
role_file.close()

#Append
role_file=open("roles.text","a")
role_file.write("I love man city")
role_file.close()

