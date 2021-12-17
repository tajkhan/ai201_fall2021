
##########################################
####	Q1A
##########################################

####	Slightly better
def has_a_repeater(*args):
	for i in range(len(args)):
		for j in range(i+1, len(args)):
			if args[i] == args[j]:
				return True
	else:
		return False

####	Relatively better
def has_a_repeater3(*args):
	if len(set(args)) < len(args):
		return True
	else:
		return False

####	Too short, perhaps?
def has_a_repeater4(*args):
	return len(set(args)) < len(args)


##########################################
####	Q2A
##########################################

####	
def find_repeaters(arg):
	repeaters = []
	for x in arg:
		if (arg.count(x) > 1) and (x not in repeaters):
			repeaters.append(x)
	return repeaters


##########################################
####	Q3A
##########################################

####	

def long_subseq(arg):
	start = 0
	end = 0

	cur_start = 0

	for i in range(len(arg)):
		if arg[i] <= arg[i-1]:
			if (i-cur_start) > (start-end):
				start = cur_start
				end = i-1

			cur_start = i
	else:
		#print(f"i={i}, curstart={cur_start}")
		#print(f"start={start}, end={end}")
		if (i-cur_start) > (end-start):
			start = cur_start
			end = i


	return arg[start:end+1]



##########################################
####	Testing code
##########################################
if __name__ == '__main__':
	print("Q1A#1")
	print(has_a_repeater(1,2,4,2,4,2))
	print(has_a_repeater("ding", "dong", 3))
	print(has_a_repeater())


	print("Q2A#1")
	print(find_repeaters([1,2,4,2,4,2]))
	print(find_repeaters(["ding", "dong", "ding", "din"]))
	print(find_repeaters([]))


	print("Q3A#1")
	seq = [2,3,4,5,2]
	#print(seq)
	print(long_subseq(seq))


	print("Q3A#2")
	seq = [2,3,4,-9,-5,-3,-1,2,3,1]
	#print(seq)
	print(long_subseq(seq))

