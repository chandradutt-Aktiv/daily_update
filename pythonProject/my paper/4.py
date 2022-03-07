"""
dictionary program
"""

x = {
	"s1": {
		"p1": {
			"Jan": {"cost": [10, 30, 45, 50], "sp": []},    # +20%
			"Feb": {"cost": [60, 64, 68], "sp": []}},       # +30%
		"p2": {
			"Jan": {"cost": [66, 67, 81, 75], "sp": []},    # +20%
			"Feb": {"cost": [78, 81, 85], "sp": []}},       # +30%
		"p3": {
			"Jan": {"cost": [18, 20], "sp": []},        # +35%
			"Feb": {"cost": [21, 22], "sp": []},        # +40%
			"March": {"cost": [22, 23, 24], "sp": []}   # +50%
			}
	},
	"s2": {
		"p1":
			{
				"Jan": {"cost": [206, 220, 225], "sp": []},     # +10%
				"March": {"cost": [180, 170, 165], "sp": []},   # +15%
				"April": {"cost": [160, 150, 136], "sp": []},   # +10%
			},
		"p4":
			{
				"Jan": {"cost": [300], "sp": []},               # +10%
				"Feb": {"cost": [280, 300, 285], "sp": []},     # +10%
				"March": {"cost": [280, 300, 285], "sp": []},   # +15%
				"April": {"cost": [360, 376], "sp": [10]}       # +10%
			},
	},
	"s3": {
		"p2":
			{
				"March": {"cost": [55, 59, 61], "sp": []},
				"April": {"cost": [53, 54, 55], "sp": []}
			}
	}
}



def a(x):
	"""
	Function is for finding sale price.
	"""
	for key, value in x.items():
		if type(value) == dict:
			a(value)
		elif len(value) > 1:
			print(value)
			for cp in value:
				per = ((cp*20)//100)
				sp = per + (for i in value)
				print(sp)
				print(per)
			
			
			
	
	# avg1 = x["s1"]["p1"]["Jan"]["cost"]
	# n = len(avg1)
	# sum=0
	# for i in avg1:
	# 	sum += i
	# avg = sum//n
	# print('average of CP: ', avg)
	# per = float(input('enter percentage of profit: '))
	# sp = (avg+(avg*per)/100)
	# print(sp)
	# set_saleprice = x["s1"]["p1"]["Jan"]["sp"] = sp
	# print(set_saleprice)
a(x)