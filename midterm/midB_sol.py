##########################################
####	Q1B
##########################################

####	Very naive implementation
def has_a_repeater(**kwargs):
	for k,v in kwargs.items():
		oncefound = False
		for k2,v2 in kwargs.items():
			if v==v2:
				if oncefound == True:
					return True
				else:
					oncefound = True
	else:
		return False


####	Slightly better
def has_a_repeater2(**kwargs):
	l1 = list(kwargs.items())
	for i in range(len(l1)):
		for j in range(i+1, len(l1)):
			if l1[i][1] == l1[j][1]:
				return True
	else:
		return False


####	Relatively better
def has_a_repeater3(**kwargs):
	l1 = list(kwargs.values())
	if len(set(l1)) < len(l1):
		return True
	else:
		return False


##########################################
####	Q2B
##########################################

####	
def find_singles(arg):
	singles = []
	for x in arg:
		if arg.count(x) == 1:
			singles.append(x)
	return singles 


##########################################
####	Q3B
##########################################

####	
def max_profit(arg):
	buyday = 0
	sellday = 0

	for i in range(len(arg)):
		for j in range(i+1, len(arg)):
			if (arg[j]-arg[i]) > (arg[sellday]-arg[buyday]):
				# found better deal; save.
				buyday = i
				sellday = j

	return buyday, sellday


if __name__ == '__main__':
	##########################################
	####	Testing code
	##########################################

	print(has_a_repeater3(v1=1,v2=2,v3=4,v4=2))
	print(has_a_repeater3(v1=1,v2="ding",v3=4))
	print(has_a_repeater3())

	print(find_singles([1,2,4,2,5,4,2]))
	print(find_singles(["ding", "dong", "ding", "din"]))
	print(find_singles([]))


	print(max_profit([7,3,6,12,5,1,4,8]))
	print(max_profit([7,3,6,9,5,1,4,8]))
	print(max_profit([7,6,5,4,1]))