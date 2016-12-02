import re


hand = open('regex_sum_303387.txt')

totallist=[]

for line in hand:

	y= re.findall('[0-9]+',line)
	totallist.extend(y)



sum =0;

for num in totallist:
	sum+= int(num)


print(sum)


