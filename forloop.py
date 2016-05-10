for i in range(1, 21):
	print i,

for i in range(1, 21):
	if i == 13:
		print "hello"
	else:
		print i



fruits = ['apples', 'oranges', 'bananas']
for fruit in fruits:
	print fruit

for fruit in range(len(fruits)):	
	print fruits[fruit]

# def sum_nums(num):
# 	sum = 0
# 	for num in range(num):
# 		sum = sum + num
# 	return sum

# def sum_nums(num):
# 	sum = 0
# 	for num in range(num+1):
# 		sum += num
# 	return sum


# Write a function called sum_nums2 that checks if the parameter num is negative. If it is, sum_nums2 should add up all of the numbers from 0 to the negative number and return that sum. If the parameter num is positive, sum_nums2 should work the same as sum_nums from #7 part A.

def sum_nums2(num):
	sum = 0
	if num < 0:
		for num in range(0,num-1,-1):
			sum += num	
	else:
		for num in range(num):
			sum = sum + num
	return sum 

print sum_nums2(-4)
