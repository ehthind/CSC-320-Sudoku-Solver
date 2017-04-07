import sys

FILE = 0

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#   convertBase9(x,y,z)
#   Converts values x,y,z to assignment specified base 9 values
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def convertBase9(x,y,z):
  return (x-1)*81 + (y-1)*9 + (z-1) + 1


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#   givenCNF(puzzle)
#
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def givenCNF(board):
  count = 0
  for x in range(9):
    for y in range(9):
      if board[x][y] != '0':
        writeToFile(str(convertBase9(x+1, y+1, int(board[x][y]))) + ' 0\n')
        count += 1
  return count


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#   rowCNF()
#
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def rowCNF():
  count = 0
  for y in range(1, 10):
    for z in range(1, 10):
      for x in range(1, 9):
        for i in range(x + 1, 10):
          writeToFile("-" + str(convertBase9(x, y, z)) + " -" +  str(convertBase9(i, y, z)) + " 0\n")
          count += 1
  return count


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#   columnCNF()
#
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def columnCNF():
  count = 0
  for x in range(1,10):
    for z in range(1, 10):
      for y in range(1,9):
        for i in range(y + 1, 10):
          writeToFile("-" + str(convertBase9(x, y, z)) + " -" + str(convertBase9(x, i, z)) + " 0\n")
          count += 1
  return count


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#   soloCNF()
#
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def soloCNF():
  count = 0
  for x in range(1, 10):
    for y in range(1, 10):
      for z in range(1, 10):
        writeToFile(str(convertBase9(x, y, z))+' ')
      writeToFile(' 0\n') # Terminate with a 0
      count += 1
  return count

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#   gen3x3CNF()
#
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def gen3X3CNF():
  count = 0
  #Turn the grid into
  for z in range(1, 10):    #Numbers from 0-8 (possible input values, in base 9)
    for gridX in range(0, 3):    #Grid (3x3 boxes) along the X axis
      for gridY in range(0, 3):  #Grid (3x3 boxes) along the Y axis
        for x in range(1, 4):
          for y in range(1, 4):

            #Minimal clauses
            for k in range(y + 1, 4):
              a = gridX * 3 + x
              b = gridY * 3 + y
              c = gridY * 3 + k
              writeToFile('-' + str(convertBase9(a,b,z)) + ' -' + str(convertBase9(a,c,z)) + ' 0\n')
              count += 1

            for k in range (x + 1, 4):
              for l in range(1, 4):
                a = gridX * 3 + x
                b = gridY * 3 + y
                c = gridX * 3 + k
                d = gridY * 3 + l
                writeToFile('-' +  str(convertBase9(a,b,z)) + ' -' + str(convertBase9(c,d,z)) + ' 0\n')
                count += 1
  return count


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#   writeToFile(string)
#
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def writeToFile(string):
    FILE.write(string)
    return


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#   parseAndFormat(filePath)
#   Formats input file into one string
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
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


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#   makeBoard(puzzle)
#   Create a 2 by 2 array with values from the input puzzle
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def makeBoard(puzzle):
  arr = [[0 for x in range(9)] for x in range(9)]
  for i in range(9):
    for j in range(9):
      arr[i][j] = puzzle[ i * 9 + j ]
  return arr


def line_prepender(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#   main()
#
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def main():

    print("Starting the SAT Solver!\n")
    if len(sys.argv) < 2:
        print("Error: Incorrect arguments")
        print("To run: python sat2sud.py <input> <minisat path>")
        sys.exit(-1)
    try:
        global FILE
        FILE = open('output_file', 'w')
    except:
        print("Unable to open file: " + 'output_file')
        sys.exit(-1)

    formatPuzzle = parseAndFormat(sys.argv[1])
    board = makeBoard(formatPuzzle)

    clauses = 0
    clauses += givenCNF(board)
    clauses += soloCNF()
    clauses += columnCNF()
    clauses += rowCNF()
    clauses += gen3X3CNF()
    FILE.close()

    filename = 'output_file'
    line = "p cnf 729 "

    newC = str(clauses)
    line += newC
    line += "\n"
    line_prepender(filename, line)

    call([sys.argv[2], filename, 'SAT_output'])

    call(['python', 'sat2sud.py', 'SAT_output'])



if __name__ == "__main__":
	main()
