import sys
import math

def printPuzzle(sudokuPuzz):
	lenOfPuzzle = len(sudokuPuzz)
	row = int(math.sqrt(lenOfPuzzle))
	sectInPuzzle=int(math.sqrt(row))
	numSect= int(row / sectInPuzzle)
	count = 0
	loop = sectInPuzzle * 3
	#iterate through number of sectors
	for makeDash in range(0,numSect):
		if makeDash != 0:
			sys.stdout.write(' ')
			#nested loops created to insert '-' for 3x3 box
			for dash in range(0, numSect):
				if dash != 0:
					sys.stdout.write('-')
				for dash2 in range(0, loop):
					sys.stdout.write('-')
			sys.stdout.write('-')
			print '-'
		#print values as well as inserting | for 3x3 box
		for section in range(0,sectInPuzzle):
			for line in range(0,numSect):
				sys.stdout.write(' |')
				for printNum in range(0,sectInPuzzle):
					sys.stdout.write("%2d" %sudokuPuzz[count])
					if printNum!= sectInPuzzle - 1:
						sys.stdout.write(" ") #space between 3x3 box
					count +=1
			sys.stdout.write(' |')
			print ' '

def main():
	try:
		file = open("final","r")
	except:
		print "Error: Cannot write to file"
		return

	sudFinal=[]
	#read file and split at space
	iterate = file.read().split(' ')
	for checkNum in iterate:
		if checkNum.isdigit() and checkNum>0:
			conv = int(checkNum)
			#convert to base 10
			baseTen = int((conv-1)%9 + 1)
			sudFinal.append(int(baseTen))
	#print final result
	printPuzzle(sudFinal)

if __name__ == "__main__":
	main()
