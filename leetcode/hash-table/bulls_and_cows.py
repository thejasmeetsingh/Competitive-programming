class Solution:
	def getHint(self, secret: str, guess: str) -> str:
		A = 0
		B = 0
		for index in range(len(secret) - 1, -1, -1):
			if secret[index] == guess[index]:
				A += 1
				secret = secret[: index] + secret[index + 1 :]
				guess = guess[: index] + guess[index + 1 :]
    
		for first in secret:
			if first in guess:
				B += 1
				guess = guess.replace(first, "", 1)

		return f"{A}A{B}B"
