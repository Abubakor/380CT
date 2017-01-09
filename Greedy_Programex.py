import random

numbers = []
left = []
right = []

def farthestVal(num):
	largest_delta = 0 
	for i in numbers:
		if(abs(num-i) > largest_delta): 
			large_key = i
	return large_key


for i in range(12):
	numbers.append(random.randrange(1,6,1))
print (numbers)
for j in range(12):
	if(balance != 0): 
		if(balance < 0): 
			far_val = farthestVal(balance) 
			right.append(far_val)
		else: 
			far_val = farthestVal(balance)  
			left.append(far_val) 
			numbers.remove(far_val)
			balance -= far_val 

print ('balance: ')
print (balance)
