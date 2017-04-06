import sys

FILE = 0

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#   convertBase4(x,y,z)
#   Converts values x,y,z to assignment specified base 4 values
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def convertBase4(x,y,z):
  return (x-1)*16 + (y-1)*4 + (z-1) + 1


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#   givenCNF(puzzle)
#
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def givenCNF(board):
  count = 0
  for x in range(4):
    for y in range(4):
      if board[x][y] != '0':
        writeToFile(str(convertBase4(x+1, y+1, int(board[x][y]))) + ' 0\n')
        count += 1
  return count


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#   rowCNF()
#
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def rowCNF():
  count = 0
  for y in range(1, 5):
    for z in range(1, 5):
      for x in range(1, 4):
        for i in range(x + 1, 5):
          writeToFile("-" + str(convertBase4(x, y, z)) + " -" +  str(convertBase4(i, y, z)) + " 0\n")
          count += 1
  return count


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#   columnCNF()
#
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def columnCNF():
  count = 0
  for x in range(1,5):
    for z in range(1, 5):
      for y in range(1,4):
        for i in range(y + 1, 5):
          writeToFile("-" + str(convertBase4(x, y, z)) + " -" + str(convertBase4(x, i, z)) + " 0\n")
          count += 1
  return count


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#   soloCNF()
#
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def soloCNF():
  count = 0
  for x in range(1, 5):
    for y in range(1, 5):
      for z in range(1, 5):
        writeToFile(str(convertBase4(x, y, z))+' ')
      writeToFile(' 0\n') # Terminate with a 0
      count += 1
  return count

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#   gen2x2CNF()
#
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def gen2X2CNF():
  count = 0
  #Turn the grid into
  for z in range(1, 5):    #Numbers from 0-3 (possible input values, in base 4)
    for gridX in range(0, 2):    #Grid (2x2 boxes) along the X axis
      for gridY in range(0, 2):  #Grid (2x2 boxes) along the Y axis
        for x in range(1, 3):
          for y in range(1, 3):

            #Minimal clauses
            for k in range(y + 1, 3):
              a = gridX * 2 + x
              b = gridY * 2 + y
              c = gridY * 2 + k
              writeToFile('-' + str(convertBase4(a,b,z)) + ' -' + str(convertBase4(a,c,z)) + ' 0\n')
              count += 1

            for k in range (x + 1, 3):
              for l in range(1, 3):
                a = gridX * 2 + x
                b = gridY * 2 + y
                c = gridX * 2 + k
                d = gridY * 2 + l
                writeToFile('-' +  str(convertBase4(a,b,z)) + ' -' + str(convertBase4(c,d,z)) + ' 0\n')
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
  arr = [[0 for x in range(4)] for x in range(4)]
  for i in range(4):
    for j in range(4):
      arr[i][j] = puzzle[ i * 4 + j ]
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
    clauses += gen2X2CNF()
    FILE.close()

    filename = 'output_file'
    line = "p cnf 729 "

    newC = str(clauses)
    line += newC
    line += "\n"
    line_prepender(filename, line)


if __name__ == "__main__":
	main()
