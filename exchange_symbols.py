__author__ = "AndySH720"

def symb_exchange(line):
	lst = list(line)
	fc = lst[0]
	lc = lst[-1]
	lst[0] = lc
	lst[-1] = fc
	lst = ''.join(lst)
	return lst
if __name__ == '__main__':
	# These "asserts" using only for self-checking and not necessary for auto-testing
	assert symb_exchange("az") == "za", "1st example";
	assert symb_exchange("aiiiiiz") == "ziiiiia", "2st example";
	assert symb_exchange("length") == "hengtl", "3st example";
	print("Code's finished? Earn rewards by clicking 'Check' to review your tests!")
