
import sys

#   parseAndFormat(filePath)
#    formats input file into one string
def parseAndFormat(filePath):

    try:
        open_file = open(filePath)
    except:
        print("Unable to open file: " + filePath)
        sys.exit(-1)

    content = open_file.readlines()
    encodedLine = ""
    for line in content:
        encodedLine += ''.join(line.split())

    #remove and replace all wildcards with 0
    encodedLine = encodedLine.replace('.', '0').replace('*', '0').replace('?', '0')
    return encodedLine

#   makeBoard(puzzle)
#    create a 2 by 2 array with values from the input puzzle
def makeBoard(puzzle):
  arr = [[0 for x in range(9)] for x in range(9)]
  for i in range(9):
    for j in range(9):
      arr[i][j] = puzzle[ i * 9 + j ]
  return arr


#   main()
#
def main():

    print("Starting the SAT Solver!\n")
    if len(sys.argv) < 2:
        print("Error: Incorrect arguments")
        print("To run: python sat2sud.py <input> <minisat path>")
        sys.exit(-1)

    formatPuzzle = parseAndFormat(sys.argv[1])
    board = makeBoard(formatPuzzle)
    print(board)


if __name__ == "__main__":
	main()
