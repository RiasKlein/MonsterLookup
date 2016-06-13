################################################################################
#
#	listToHTML.py
#
#	Outputs an HTML file containing all the entries of a provided input file
#	
################################################################################

import sys

def listToHTML ( in_filename, out_filename, out_title ):
	# Open the file to read from
	rfile = open ( in_filename, 'r' )

	# Create/open the output file
	wfile = open ( out_filename, 'w' )
	
	############################################################################
	#	Write the basic start of the HTML output file
	############################################################################
	
	wfile.write(
"""<!DOCTYPE html> <html> <body>

""")

	if out_title != "":
		wfile.write ("<h2>")
		wfile.write ( out_title )
		wfile.write ("</h2>")
		
	wfile.write (
"""

<ul style="list-style-type:none">""")

	wfile.write ("<title>")
	wfile.write ( out_title )
	wfile.write ("</title>")

	############################################################################
	#	Start reading from the input file and writing that into output
	############################################################################
	
	while True:
		line = rfile.readline()
		if not line: break
		
		if '.txt' not in line:
			line = line[:-6]	# Strip the '.html\n' from each of the entries
			
			# Capitalize the first letter of every word in the name
			list = [word[0].upper() + word[1:] for word in line.split()]
			line = " ".join(list)
			
			wfile.write ("""
	<li>""")
			wfile.write (line)
			wfile.write ("</li>")
			
	############################################################################
	#	Write the basic ending of the HTML output file
	############################################################################
	
	wfile.write (""" 
</ul> </body> </html>
""")
			
	wfile.close()
	rfile.close()
