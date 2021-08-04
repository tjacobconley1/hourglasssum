
import sys


# function to calculate hgs
# the row and column are passed so that the function
# can be called within the nested for loop below
def gethourglasssum(array, r, c):
	sum = 0
	sum += array[r -1][c - 1]
	sum += array[r -1][c]
	sum += array[r - 1][c + 1]
	sum += array[r][c]
	sum += array[r + 1][c - 1]
	sum += array[r + 1][c]
	sum += array[r + 1][c + 1]
	return sum


arr = []

