def aa(a,b,c):
	for i in a:
		if(i in b.keys()):
			c.append(i)
			c.append(b[i])
			print(c)
		aa(a,b,c)
a = [1,2,3]

b = {
	1: [4,5,6],
	2: [7,8],
	3: [9, 10],
	4: [11, 12, 13],
	9: [14, 15],
	10: [16],
	13: [19, 20],
	19: [21]
}
c=[]
print(aa(a,b,c))
"""
for i in a:
	c.append(i)
	if(i in b.keys()):
		#print(i)
		for j in b[i]:
			print(j)
			c.append(j)
			if(j in b.keys()):
				print(j)"""