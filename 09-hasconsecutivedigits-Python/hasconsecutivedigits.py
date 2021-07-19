# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that 
# number contains two consecutive digits that are the same, and False otherwise.

def hasconsecutivedigits(n):
	if abs(n) < 10: 
		return False
	n = abs(n)
	lastDigit = -1
	while n > 0:
		currentDigit =  n % 10
		if currentDigit == lastDigit: 
			return True
		lastDigit = currentDigit  
		n //= 10                  
	return False