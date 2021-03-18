a = int(input("enter the limit"))
c=65
for x in range(1,a+1):
	for y in range(0,x):
	    print(chr(c),end='  ')
	    c=c+1
	print()

