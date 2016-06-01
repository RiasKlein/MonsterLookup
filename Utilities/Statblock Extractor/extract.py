################################################################################
#
#	extract.py
#	Program extracts statblock5e code from an input file to a specified output file
#
#	Usage: 	python extract.py [file with statblock code] [output filename]
#			python extract.py [file with statblock code]
#
#	Program written by: Shunman Tse
#
################################################################################

import sys

output_filename = 'output.txt'

# Use the provided filename if there is one
if len(sys.argv) > 2:
	output_filename = sys.argv [2]

# Check to see if we have a provided file
if len(sys.argv) < 2:
	print ("Usage Error:\t\tThe program needs an input file to run.")
	print ("Correct Usage:\t\tpython extract.py [input filename]")
	print ("Alternate Usage:\tpython extract.py [input filename] [output filename]")
	sys.exit(1)
	
def extractStatblock ( rfile, wfile ):
	# Start reading the input file one line at a time until we find 
	#	the starting point of the statblock code
	while True:
		line = rfile.readline()
		if not line: return
		
		# Once we find the start of the statblock code, copy each line from
		#	the input file to the output file until we see the end of the 
		#	statblock code
		if '<stat-block>' in line:
			wfile.write (line)		
			while True:
				line = rfile.readline()
				if not line: return
				
				if '</stat-block>' in line:
					wfile.write ('</stat-block>')
					return
					
				wfile.write(line)
				
def main():
	rfile = open (sys.argv[1], 'r')
	wfile = open (output_filename, 'w')

	extractStatblock (rfile, wfile)

	# Close the files now that we are done
	rfile.close()
	wfile.close()
	
main()

	
	
