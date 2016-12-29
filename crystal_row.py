__author__ = "AndySH720"

# This program wouldn't work well enough in real life, but for this task it does the job just fine

def check_line(line):
	if line[1:] == line[:-1]:
		return False
	if len(line) < 6:
		while len(line) <= 6:
			if line[-1] is "X":
				line.append("Z")
			elif line [-1] is "Z":
				line.append("X")
	if line[1] is line[3] and line[2] is line[4] and line[3] is line[5] and line[4] is line[6] and line[-1] is line[-3] and line[-2] is line[-4]:
		return True
	else:
		return False
if __name__ == '__main__':
	# These "asserts" using only for self-checking and not necessary for auto-testing
	assert check_line(["X", "Z", "X"]) == True
	assert check_line(["X", "Z", "X", "X"]) == False
	assert check_line(["X", "Z"]) == True
	assert check_line(["Z", "X"]) == True
	assert check_line(["Z", "X", "Z", "X", "Z", "Z", "X"]) == False
	print("Code's finished? Earn rewards by clicking 'Check' to review your tests!")
