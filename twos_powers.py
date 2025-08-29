def twos_powers(n):
	if n & n-1 == 0:
		return True
	else:
		return False
n = int(input("Enter your number : "))

print(twos_powers(n))