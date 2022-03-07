#!/bin/python3

# import math
# import os
# import random
# import re
# import sys
from collections import Counter


#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def checkMagazine(magazine, note):
	if((Counter(note) - Counter(magazine)) == {}):
		print('Yes')
	else:
		print('No')
	
	


if __name__ == '__main__':
	# first_multiple_input = input().rstrip().split()

	# m = int(first_multiple_input[0])
	#
	# n = int(first_multiple_input[1])

	magazine = 'two times three is not four'.rstrip().split()

	note = 'two times two is four'.rstrip().split()

	checkMagazine(magazine, note)
# Write your code here
# cyes = 0
# cno = 0

# for i in magazine:
#     for j in note:
#         if(j == i):
#             cyes += 1
#             i += i
#             # print('Yes')
#         else:
#             cno += 1
#             # print('No')

# if(cyes == len(note)):
#     print('Yes')
# else:
#     print('No')
# print(magazine)
# print(note)

# if __name__ == '__main__':
# 	first_multiple_input = input().rstrip().split()
#
# 	m = int(first_multiple_input[0])
#
# 	n = int(first_multiple_input[1])
#
# 	magazine = input().rstrip().split()
#
# 	note = input().rstrip().split()
#
# 	checkMagazine(magazine, note)

# #!/bin/python3
#
# import math
# import os
# import random
# import re
# import sys
#
#
# #
# # Complete the 'checkMagazine' function below.
# #
# # The function accepts following parameters:
# #  1. STRING_ARRAY magazine
# #  2. STRING_ARRAY note
# #
#
# def checkMagazine(magazine, note):
# 	# Write your code here
# 	cyes = 0
# 	cno = 0
#
# 	for i in magazine:
# 		for j in note:
# 			if (j == i):
# 				cyes += 1
# 				i += i
# 			# print('Yes')
# 			else:
# 				cno += 1
# 			# print('No')
#
# 	if (cyes == len(note)):
# 		print('Yes')
# 	else:
# 		print('No')
#
#
# # print(magazine)
# # print(note)
#

