a = int(input("enter the limit"))
for x in range(a):
	for y in range(65,65+x+1):
		print(chr(y),end=' ')
	print()

