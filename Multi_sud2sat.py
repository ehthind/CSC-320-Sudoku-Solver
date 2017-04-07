import sys
import os
from subprocess import call


FILE = 0
encoded_files = []
SAT_files = []


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

  for z in range(1, 10):
    for xAxis in range(0, 3):
      for yAxis in range(0, 3):
        for x in range(1, 4):
          for y in range(1, 4):

            #Minimal clauses
            for k in range(y + 1, 4):
              a = xAxis * 3 + x
              b = yAxis * 3 + y
              c = yAxis * 3 + k
              writeToFile('-' + str(convertBase9(a,b,z)) + ' -' + str(convertBase9(a,c,z)) + ' 0\n')
              count += 1

            for k in range (x + 1, 4):
              for l in range(1, 4):
                a = xAxis * 3 + x
                b = yAxis * 3 + y
                c = xAxis * 3 + k
                d = yAxis * 3 + l
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
    puzzle_list = []
    try:
        fp = open(filePath)
    except:
        print("Unable to open file: " + filePath)
        sys.exit(-1)

    L = ''
    temp = 0
    for i, line in enumerate(fp):

        if i%10 != 0:
            # line we need
            L += ''.join(line.split())
        elif i == 0:
            # first line we skip
            temp += 1
        else:
            # line we should save and skip
            L = L.replace('.', '0').replace('*', '0').replace('?', '0')
            puzzle_list.append(L)
            K = ''
            L = K

    fp.close()
    '''
    content = open_file.readlines()
    encodedLine = ""
    for line in content:
        encodedLine += ''.join(line.split())

    #remove and replace all wildcards with 0
    encodedLine = encodedLine.replace('.', '0').replace('*', '0').replace('?', '0')
    '''
    return puzzle_list


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

    # ensure proper system arguments
    if len(sys.argv) < 2:
        print("Error: Incorrect arguments")
        print("To run: python sat2sud.py <input> <minisat path>")
        sys.exit(-1)

    formatPuzzleList = parseAndFormat(sys.argv[1])

    encoded_filename = ''

    puzzle_count = 1
    for puzzle in formatPuzzleList:
        encoded_filename = ''.join(('encoded_puzzles/encoded_puzzle_',str(puzzle_count)))
        encoded_files.append(encoded_filename)

        try:
            global FILE
            FILE = open(encoded_filename, 'w')
        except:
            print("Unable to open file: " + 'encoded_filename')
            sys.exit(-1)

        #make clauses
        board = makeBoard(puzzle)
        clauses = 0
        clauses += givenCNF(board)
        clauses += soloCNF()
        clauses += columnCNF()
        clauses += rowCNF()
        clauses += gen3X3CNF()

        FILE.close()

        #prepend 'p cnf <# variables> <# clauses>' to file
        pre_filename = encoded_filename
        line = "p cnf 729 "
        newC = str(clauses)
        line += newC
        line += "\n"
        line_prepender(pre_filename, line)

        puzzle_count += 1


        output_count = 1

    for encoded in encoded_files:
        SAT_output_file = ''.join(('SAT_solved_puzzles/SAT_output_puzzle_',str(output_count)))
        call([sys.argv[2], encoded, SAT_output_file, '>', 'minisat_output.txt'])
        SAT_files.append(SAT_output_file)
        output_count += 1


    for SAT_file in SAT_files:
        call(['python', 'sat2sud.py', SAT_file])



if __name__ == "__main__":
	main()
