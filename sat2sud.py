import sys
import math

FILE = 0

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
					#FILE.append('-')
					sys.stdout.write('-')
				for dash in range(0, loop):
					#FILE.append('-')
					sys.stdout.write('-')
			#FILE.append('-')
			print('-')

		for line in range(0, sect):
			for currVal in range(0,numberOfsects):
				#FILE.append('|')
				sys.stdout.write('|')
				for number in range(0, sect):
					#FILE.append(currPuzz[inc])
					sys.stdout.write("%2d"% currPuzz[inc])
					if number != sect- 1:
						#FILE.append(' ')
						sys.stdout.write(" ")
					inc += 1
			#FILE.append('|')
			print '|'


def main():
	try:    
		global FILE
		FILE = open(sys.argv[1])
	except:
		print "Error: Cannot write to file"
		return
	finalPuzz = []
	for currNum in FILE.read().split():
		if currNum.isdigit() and currNum> 0:
			checkNum = int(currNum)
			convToBTen = int((checkNum- 1)%9 + 1)
			finalPuzz.append(convToBTen)
	#print final result
	printPuzzle(finalPuzz)

if __name__ == "__main__":
	main()
