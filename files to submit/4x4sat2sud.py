import sys
import math

def printPuzzle(currPuzz):
	lenOfPuzz = len(currPuzz)
	rowInPuzz = int(math.sqrt(lenOfPuzz))
	sect = int(math.sqrt(rowInPuzz))
	numberOfsects = int(rowInPuzz/sect)
	inc = 0
	loop =(sect*3)-1
	for value in range(0, numberOfsects):
		if value != 0:
			sys.stdout.write('-')

			for currVal in range(0, numberOfsects):
				if currVal != 0:
					sys.stdout.write('-')
				for dash in range(0, loop):
					sys.stdout.write('-')
			print '-'

		for line in range(0, sect):
			for currVal in range(0,numberOfsects):
				sys.stdout.write('|')
				for number in range(0, sect):
					sys.stdout.write("%2d"% currPuzz[inc])
					if number != sect- 1:
						sys.stdout.write(" ")
					inc += 1
			print '|'


def main():
	try:
		file = open(sys.argv[1])
	except:
		print "Error: Cannot write to file"
		return
	finalPuzz = []
	for currNum in file.read().split():
		if currNum.isdigit() and currNum> 0:
			checkNum = int(currNum)
			convToBFive = int((checkNum- 1)%4 + 1)
			finalPuzz.append(convToBFive)
	#print final result
	printPuzzle(finalPuzz)

	solved_puzzle = ''
	solved_puzzle = ''.join((sys.argv[1],'_SOLVED'))
	try:
		file = open(solved_puzzle, 'w')
	except:
		print('unable to open file')
		sys.exit(-1)
	file.write(str(finalPuzz))

if __name__ == "__main__":
	main()
