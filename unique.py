list1=[1,1,2,3,4,4,5,6,7,5,2,8]
'''n = int(input("Enter length of LIST"))
print 'Enter List elements :'
list1= [list1[i] for i in range(0,n) list1[i]=int(input("Enter value ",i," :"))]'''
unique1 = []
for i in range(0,len(list1)):
	if list1[i] not in unique1:
		unique1.append(list1[i])
print(unique1)


