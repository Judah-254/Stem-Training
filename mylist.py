other_list=[]
my_list=[2,5,3,11,1,10,6,8,4]
for elem in my_list:
    other_list.append(elem)
    print (other_list)
my_list=[2,3,5,6,7]
other_list=[elem for elem in my_list]
print (other_list)
my_list=[2,5,3,11,1,10,6,8,4]
for elem in my_list:
    if elem %2==0:
        other_list.append(elem)
print (other_list)

my_list=[2,3,4,5,6,7]
other_list=[elem for elem in my_list if elem %2==0]
print (other_list)
