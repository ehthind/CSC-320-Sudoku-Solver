import sys

out_stdout = sys.stdout #takes what ever is printed to the console and writes 
f = open('output_CNF.txt', 'w') #to the file
sys.stdout = f

###############

#place code to convert sudoku to CNF grammer below#

###############

def encoder( i, j, k):
	Val = 81*(i-1) + 9*(j-1)+(k-1) + 1
	print Val,
	return

#cnf_Printer function is for debugging currently, select a value 1-10 for rows 
#and columns to determine which cells to print to output for col i pass i+1 to 
#printer. Currently it assumes 1-9 can possibly work in each cell. Pass k 10
def cnf_Printer( row_range, col_range, val_range):
	for i in range(1,row_range):
		for j in range(1,col_range):
			print 'c Cell', (i,j), 'contains at least one number'
			for k in range(1,val_range): #change this, no 3 loop
				encoder(i,j,k);
			print 0
	return

cnf_Printer(10,10,10);
		
##############

#end of code for conversion#

##############


sys.stdout = out_stdout #closes the output file
f.close()
