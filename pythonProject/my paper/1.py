l = ['zios','1n@','adfi']

for i in l:
	if(i[0].islower() and i[0] not in 'aeiou'):
		if(i.isalpha()):
			print(i)