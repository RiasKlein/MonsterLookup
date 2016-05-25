################################################################################
#
#	run.py
#	Generates statblock HTML files for monsters with a provided input file
#
#	Usage: python run.py [monster name] [monster info file name]
#	
#	This generator is developed by Shunman Tse (RiasKlein)
#		https://github.com/riasklein
#	Statblock5e code is by Val Markovic (Valloric) 
#		https://github.com/Valloric
#
#	Version 0.8
#
################################################################################

import sys
from Helpers.genFormatting import genFormatting
from Helpers.genStatblock import genStatblock

def print_usage_instructions():
	print ("Correct Usage:\tpython run.py [monster name] [info file name]")

if len(sys.argv) < 3:
	print ("Usage Error: bestiaryGen.py cannot run properly")
	print_usage_instructions()
	sys.exit()
	
file_name = genFormatting (sys.argv[1])
genStatblock (sys.argv[1], sys.argv[2])

# Add the ending to the file
wfile = open (file_name, 'a+')
wfile.write ("</body></html>")
wfile.close()


