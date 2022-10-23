#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Run a simple analysis of the equation, 3x+1.
This is a recursive function in which it is defined in a system by the following.

f(x)  = {3x+1} if f(x) is odd
f(x)  = (f(x)/2) if f(x) is even.

"""

import sys
import threeXPlusOne_helper as gh

# Running in a virtual environment:
# virtualenv myenv -p python3
# source myenv/bin/activate
# python3 threeXPlusOne.py -h

dir_str = "0_out/"
# addPos_bol = True # add the position numbers in the output CSV files
addPos_bol = False # Do not add the position numbers in the output CSV files

def getArguments(argv_list):
	""" A function to determine what parameters have been entered and then completed tasks  """

	# print(argv_list)

	param_2 = "-H" # call for helper()
	param_3 = "-N" # Give seed number and get sequence
	param_4 = "-C" # call for a count down from a number
	param_5 = "-E" # print up extra help or add an option here.

	if len(argv_list) == 0:
			# Output welcome message
			# print(printWithColour(BICyan,gh.WHATISTHIS_p1))
			print(gh.printWithColour(gh.BICyan, gh.WHATISTHIS_p2))

	helperFlag_Bool = False
	for i in argv_list:
		if param_2 == i.upper():
			# print(f"\t Call to help found: {i}")
			helperFlag_Bool = True
			gh.helper()
			exit()

		if param_3 in i.upper():# and isinstance(i, int): # run the program with chosen number
			print(gh.printWithColour(gh.BIGreen,f" Single interation of integer {param_3}"))
			try:
				begin(int(argv_list[1])) #  ['-n', '8']
			except IndexError:
				print(gh.printWithColour(gh.BIRed,"\t [-] No valid integer entered."))
			except ValueError:
				print(gh.printWithColour(gh.BIRed,"\t [-] No valid integer entered."))
			exit()

		if param_4 in i.upper(): # count down from a user-specified value
			try:
				print(gh.printWithColour(gh.BIGreen,f"\t [+] Counting down from integer {argv_list[1]}"))
				try:
					countDown(int(argv_list[1]))
				except ValueError:
					print(gh.printWithColour(gh.BIRed,f"\t [-] Not a valid integer: {argv_list[1]}"))
			except IndexError:
				print(gh.printWithColour(gh.BIRed,"\t [-] No valid integer entered."))
			exit()


		if param_2 not in i.upper() and param_3 not in i.upper() and param_4 not in i.upper() and param_5 not in i.upper():
			print(gh.printWithColour(gh.BICyan, gh.WHATISTHIS_p2))
			exit()

# end of getArguments()

def countDown(in_int):
	""" function to call doTheMath() for a user-specificed number of times."""
	print(gh.printWithColour(gh.BICyan,f"\t [+] preparing all sequences from a count of 1 to {in_int}"))

	for i in range(1,in_int + 1,1):
		print(gh.printWithColour(gh.BICyan,f"\n\t ___ Number {i} ___"))
		begin(i)

# print command to stack all these output files together in bash code.
# paste * | cut -f 1,2,3,4,5,6,7,8,9,10

	tmp = ""
	for i in range(1,in_int+1,1): tmp = tmp + f"{i},"
	tmp = tmp[:len(tmp)-1] #remove the end comma

	print(gh.printWithColour(gh.BICyan,f"\n\t [+] Combine these files into one for easy plotting:"))
	print(gh.printWithColour(gh.BICyan,f"\t paste {dir_str}* | cut -f {tmp} > {dir_str}data_{in_int}.csv"))
# end of countDown()



def doTheMath(mySeedNumer_int):
	""" Driver function for the math experiment using the seed number. """

	myResult = mySeedNumer_int
	numSeq_dic = {}
	counter = 0
	maxValue_int = 0 # largest value of sequence


	while myResult != 1:
		# print(gh.printWithColour(gh.BIYellow,f"\t [+] myResult: {myResult}"))

		if int(myResult % 2) == 0: #even?
			print(gh.printWithColour(gh.BIYellow,f"\t   {counter},  {myResult}"),gh.printWithColour(gh.BIGreen,f"\t even"))
			myResult = int(myResult /2)

			numSeq_dic[counter] = myResult

		elif myResult % 2 == 1: #odd?
			print(gh.printWithColour(gh.BIYellow,f"\t   {counter},  {myResult}"),gh.printWithColour(gh.BIRed,f"\t odd"))
			myResult = int((myResult * 3) + 1)
			numSeq_dic[counter] = myResult

		counter = counter + 1
		if myResult > maxValue_int:
			maxValue_int = myResult

	print(gh.printWithColour(gh.BIYellow,f"\n\t [+] Completed at {myResult}, MaxValue = {maxValue_int}"))

	# print(numSeq_dic)
	return numSeq_dic
# end of doTheMath()

def begin(myNumber_int):
	"""Driver function"""
	# print("\nbegin()")
	print(gh.printWithColour(gh.BIYellow,f"\n\t [+] Seed Number: {myNumber_int}"))
	# exit()

	# print(gh.printWithColour(gh.BIGreen,f"\t Running ..."))

	numSeq_dic = doTheMath(myNumber_int)#call on driver function for the math experiment.

	makeCSV(numSeq_dic, str(myNumber_int)+"_sequence.txt", myNumber_int) # prep data as csv for plotting, the addPos_bol parameter means to add positions to the file when set to true.
#end of begin()

def makeCSV(numSeq_dic, myFileName_str, myNumber_int):
	""" function to save a csv file of data."""

	if addPos_bol == True:
		tmp_str = f"Num, Value_{myNumber_int}\n"
	else:
		tmp_str = f"Value_{myNumber_int}\n"

	for i in numSeq_dic:
		if addPos_bol == True:
			tmp_str = tmp_str + f"{i},{numSeq_dic[i]}\n"
		else:
			tmp_str = tmp_str + f"{numSeq_dic[i]}\n"
	# print(tmp_str)

	gh.checkDataDir(dir_str) # does the data directory exist? if not make it exist
	pathFileName_str =  dir_str + myFileName_str
	# print(pathFileName_str)
	with open(pathFileName_str, 'w') as f:
			f.write(tmp_str)
	print(gh.printWithColour(gh.BIGreen,f"\t [+] CSV file saved to {pathFileName_str} "))

#end of makeCSV()

if __name__ == '__main__':
	getArguments(sys.argv[1:])
