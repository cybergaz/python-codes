# lets take a example of - 7
# 1 0 0 0 1 0 1

# 1 |0 0 0 1| 0 1
# 1 0 |0 0 1| 0 1
# 1 0 0 |0 1| 0 1
# 1 0 0 0 |1| 0 1

# 1 |0 0 0 1 0| 1
# 1 0 |0 0 1 0| 1
# 1 0 0 |0 1 0| 1
# 1 0 0 0 |1 0| 1



a = int(input("no. of piece of cake : "))
b = list(map(int,input("enter the presence of cherry for each piece (space seperated) : ").split()))

#def piece_maker(list1,list2): #list2 is the list of all the combination that have made already 

# take out number of 1's , with their indexes

list1 = []
for x in range(len(b)):
	if b[x]==1:
		list1.append(x)

z = 1
for x in range(len(list1)-1):
	y = list1[x+1]-list1[x]  #number of conditions with 0's 
	z = z*y
print("number of ways will be : ",z)

#print("their are", len(list1),"1's and their indeces are",list1,"respectively")


# take out the number of 0's between each 1 than add +1 in it and then multiply it with next number of 0's between next 1's


