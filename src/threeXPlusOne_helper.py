#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Further Learning
* Wikipedia: Collatz Conjecture
  + https://en.wikipedia.org/wiki/Collatz_conjecture

* The Simplest Math Problem No One Can Solve - Collatz Conjecture
  + https://www.youtube.com/watch?v=094y1Z2wpJg

* UNCRACKABLE? The Collatz Conjecture - Numberphile
  + https://www.youtube.com/watch?v=5mFpVDpKX70

"""

# import numpy as np
# from scipy.io import wavfile
import sys, random, os, math
from itertools import permutations
import itertools


DATE = "22 Oct 2022"
VERSION = "0.3.0"
AUTHOR = "Oliver Bonham-Carter"
AUTHORMAIL = "obonhamcarter@allegheny.edu"
THISPROG = sys.argv[0].replace("./","")
WHATISTHIS_p1 = f"""\n\t{THISPROG}: A 3x+1 sequence generator to demonstrate the Collatz Conjecture
\t Rules: x = seedNumber
\t f(x) = 3x+1.
\t If f(x) is odd, f(f(x)) = 3(f(x) + 1) + 1,
\t else, f(x) = f(x) /2.
\t Repeat until f(x) = 4, then f(x) = 2 then f(x) = 1 (stop!)
"""
WHATISTHIS_p2 = "\t Use option '-h' for more glorification about this amazing project!\n"

MYOUTPUT_DIR = "0_out/" # all results are saved in this local directory

# PAIRINGFILE = "pairings.txt" # the file containing all information about which gradebook file blongs to what gradebook repository. Note, the names of each the user and the user's gradebook file may not be the same.
# REPOFILE = "dirNames" # file to run the bulk pusher. Contains path and name of each repository to push.



# colour codes

# Bold High Intensity
BIBlack='\033[1;90m'      # Black
BIRed='\033[1;91m'        # Red
BIGreen='\033[1;92m'      # Green
BIYellow='\033[1;93m'     # Yellow
BIBlue='\033[1;94m'       # Blue
BIPurple='\033[1;95m'     # Purple
BICyan='\033[1;96m'       # Cyan
BIWhite='\033[1;97m'      # White

# Regular Colors
Black='\033[0;30m'        # Black
Red='\033[0;31m'          # Red
Green='\033[0;32m'        # Green
Yellow='\033[0;33m'       # Yellow
Blue='\033[0;34m'         # Blue
Purple='\033[0;35m'       # Purple
Cyan='\033[0;36m'         # Cyan
White='\033[0;37m'        # White

# Bold
BBlack='\033[1;30m'       # Black
BRed='\033[1;31m'         # Red
BGreen='\033[1;32m'       # Green
BYellow='\033[1;33m'      # Yellow
BBlue='\033[1;34m'        # Blue
BPurple='\033[1;35m'      # Purple
BCyan='\033[1;36m'        # Cyan
BWhite='\033[1;37m'       # White


# Bold colour list
colour_list =['\033[1;30m',
'\033[1;31m',
'\033[1;32m',
'\033[1;33m',
'\033[1;34m',
'\033[1;35m',
'\033[1;36m',
'\033[1;37m',
'\033[1;90m',
'\033[1;91m',
'\033[1;92m',
'\033[1;93m',
'\033[1;94m',
'\033[1;95m',
'\033[1;96m',
'\033[1;97m']



banner1_str = """
  ██████╗     ██╗  ██╗    ██████╗ ██╗     ██╗   ██╗███████╗     ██╗
  ╚════██╗    ╚██╗██╔╝    ██╔══██╗██║     ██║   ██║██╔════╝    ███║
   █████╔╝     ╚███╔╝     ██████╔╝██║     ██║   ██║███████╗    ╚██║
   ╚═══██╗     ██╔██╗     ██╔═══╝ ██║     ██║   ██║╚════██║     ██║
  ██████╔╝    ██╔╝ ██╗    ██║     ███████╗╚██████╔╝███████║     ██║
  ╚═════╝     ╚═╝  ╚═╝    ╚═╝     ╚══════╝ ╚═════╝ ╚══════╝     ╚═╝

"""


# banner ref: https://manytools.org/hacker-tools/ascii-banner/
# style: ASCII text banners

def checkDataDir(dir_str):
#function to determine whether a data output directory exists.
#if the directory doesnt exist, then it is created

	try:
		os.makedirs(dir_str)
		#if MYOUTPUT_DIR doesn't exist, create directory
		#printByPlatform("\t Creating :{}".format(dir_str))
		return 1

	except OSError:
		#printErrorByPlatform("\t Error creating directory or directory already present ... ")
		return 0
#end of checkDataDir()

def get_platformType():
	"""Function to dermine the OS type."""
	platforms = {
	'darwin' : 'OSX',
	'win32'  : 'Windows',
	'linux1' : 'Linux',
	'linux2' : 'Linux'}
	if sys.platform not in platforms:
		return sys.platform
	return platforms[sys.platform]
#end of get_platformType()

def printWithColour(colCode_str, myMessage_str):
	"""A function to print with colour for Unix and MacOS."""
	platform_str = get_platformType()
	if platform_str.lower() == "linux" or platform_str.lower() == "osx":
		myMessage_str = colCode_str + myMessage_str + BIWhite
		# print(colCode_str + myMessage_str + BIWhite)
	else: # Windows does not seem to like these colourcodes
		# print(myMessage_str)
		pass
	return myMessage_str
# end of printWithColour()


def bannerScreen(myCount_int):
	"""prints a charming and colourful little message for the user"""
	# report the perceived OS type
	platform_str = get_platformType()

	if platform_str.lower() == "linux" or platform_str.lower() == "osx":
		for i in range(myCount_int):
			randomColour_str = random.choice(colour_list) # choose a random colour to display the title screen.
			print(randomColour_str + banner1_str + BIWhite)
	else:
		print(banner1_str)
#end of bannerScreen()

def helper():
	"""Cheap and friendly online help; how to use the program"""
	bannerScreen(1) # print up one banner screen
	print(WHATISTHIS_p1)
	h_str1 = "\t"+DATE+" | version: "+VERSION
	h_str2 = "\t"+AUTHOR +"\n\tmail: "+AUTHORMAIL
	print("\t"+len(h_str2) * "-")
	print(printWithColour(BIYellow,h_str1))
	print("\t"+len(h_str2) * "-")
	print(printWithColour(BIBlue,h_str2))
	#print(h_str2)
	print("\t"+len(h_str2) * "-")
	print("\tOptions:")
	print(printWithColour(BIGreen,f"\t[+]"),printWithColour(BICyan,f"[-H]"),printWithColour(BIYellow,"This page, right?"))
	print(printWithColour(BIGreen,f"\t[+]"),printWithColour(BICyan,"[-N]"),printWithColour(BIYellow,"Seed number to build a sequence"))
	print(printWithColour(BIGreen,f"\t[+]"),printWithColour(BICyan,"[-C]"),printWithColour(BIYellow,"Count down from a number to build all sequences,\n\t\t make file for each."))
	print(printWithColour(BIBlue, f"\n\t[+] If you want to produce a single sequence from starting value."))
	print(printWithColour(BIGreen,f"\t[+] \U0001f600 USAGE: ./{THISPROG} -n seedNumber"))
	print(printWithColour(BIBlue, f"\n\t[+] If you want to produce all sequences from 0 to a value,\n\t  then the next option is right up your alley."))
	print(printWithColour(BIGreen,f"\t[+] \U0001f600 USAGE: ./{THISPROG} -c countDownNumber"))

#end of helper()

