__author__ = "AndySH720"

def count_units(number):
	n = bin(number)
	n = list(n)
	n = [x for x in n if x == '1']
	return len(n)
if __name__ == '__main__':
    	# These "asserts" using only for self-checking and not necessary for auto-testing
	assert count_units(4) == 1
	assert count_units(15) == 4
	assert count_units(1) == 1
	assert count_units(1022) == 9
	print("Use 'Check' to earn sweet rewards!")
