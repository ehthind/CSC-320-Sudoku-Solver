# CSC-320-Sudoku-Solver

Amrit Thind V00779722
Keifer Edelmayer V00778104
Jacqueline Reynolds V00794417
Shikha Bose V00834561

All files present:
-4x4sud2sat.py
-4x4sat2sud.py
-sud2sat.py
-sat2sud.py
-hard_solved_puzzles
-Hard Input Statistics
-Multi_sud2sat.py
-README.md

Descriptions:

4x4sud2sat.py:
-takes in a 4x4 sudoku and outputs the CNF clauses in format to be used by the minisat
-also pipes the output into minisat and calls/passes 4x4sat2sud.py its output

4x4sat2sud.py:
-takes the output from the mini sat of a 4x4 sudoku and outputs the solved sudoku

sud2sat:
-takes in a 9x9 sudoku and outputs the CNF clauses in format to be used by the minisat
-also pipes the output into minisat and calls/passes sat2sud.py its output

sat2sud.py:
-takes the out put from the mini sat of a 4x4 sudoku and outputs the solved sudoku

hard_solved_puzzles:
-solved hard puzzles

Hard Input Statistics:
-stats to the above puzzle solutions

Multi_sud2sat.py:
-modified sud2sat.py to handle multi line input, the file passed in is read line by line performing the encoding, solving via mini sat then decoding one at a time. The Multi_sat2sud.py file provides this functionality


Instructions:

Run the command: python sud2sat.py <Input file> <Path to minisat>

*sud2sat will take the input, enocde it, and then provide it to minisat and take the corresponding output and call sat2sud.py to output a solved sudoku.

*4x4sat2sud.py works the same way, call the command:

python 4x4sud2sat.py <Inpput file> <Path to minisat>


