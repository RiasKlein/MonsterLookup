import os, sys, webbrowser
from Modules.listToHTML import listToHTML

# Configurable Global Settings
file_monster_list = 'monster_list.txt'	# file with the monster HTML file names
html_monster_list_fname = 'monster_list.html'
html_monster_list_header = "Monster List"
system_version = '0.12'

# readMonsterList
#	Function reads the file monster_list.txt for all currently available monsters
#	Each entry is added into the list called monster_list
def readMonsterList ():
	# Open 'monster_list.txt' in reading mode
	rfile = open (file_monster_list, 'r')
	
	# We'll keep going until we reach the end of the file
	while True:
		line = rfile.readline()		# Get a line from 'monster_list.txt'
		if not line: return			# End the function if we're at the end

		# Only add .html files because those contain the monster files
		if ('.html' in line):
			line = line.rstrip ('\n')			# Remove the trailing new line
			line = line[:-5]					# Get rid of the .html
			monster_list.append (line.lower())	# Append as entry into the list of monsters

# handleBuiltIn
#	Function handles the built-in functions	
#	Returns whether the provided input is a built-in function	
def handleBuiltIn ( user_input ):
	is_builtin = False

	# If the input was 'help', then provide the available monster list
	if (user_input.lower() == 'help'):
		is_builtin = True
		"""
		print ("============================\n\tMonster List\n============================")
		print (monster_list)
		print ("")
		print ("System Version: " + system_version)
		"""

		# Open the HTML file with the monster names
		webbrowser.open_new_tab (html_monster_list_fname)	
		
		print ("System Version: " + system_version)
	# If the input was an empty string, then do nothing
	elif (user_input.lower() == ""):
		return True
	# If the input was 'exit', then exit the system
	elif (user_input.lower() == 'exit'):
		print ("Exiting...")
		
		# Remove the generated monster_list HTML
		os.remove (html_monster_list_fname)
		
		sys.exit()
		
	return is_builtin

# searchAndOpen
#	Function opens the monster file for the monster if it exists
#	Feedback is given regardless
def searchAndOpen ( user_input ):
	# See if the monster name is available in the monster list
	if user_input.lower() in monster_list:
		# If the monster name is found in the list of monsters: 
		#	Open the proper file in the browser
		name = user_input + '.html'
		webbrowser.open_new_tab (name)	
	else:
		# If the monster name was not found, then give output saying so
		print ("Monster Not Found")

# printIntroduction
#	Function prints out basic information displayed at the start		
def printIntroduction ():
	print ("========================= D&D 5e Monster Lookup =========================")
	print ("Type in a monster name to look for or type in 'help' for more information")
		
def main():
	# Setting the title for the program
	os.system ("title Dungeons and Dragons 5e Monster Lookup")

	# Change the working directory to the Monsters folder
	os.chdir ('./Monsters')

	# Get the names of all available monsters
	readMonsterList()
	
	# Create an updated HTML file to display all the available monsters
	listToHTML ( file_monster_list, html_monster_list_fname, html_monster_list_header)
	
	# Introduction Information!
	printIntroduction ()
	
	# Get user searches until they are done
	while True:
		# Ask the user for what they are searching for
		sys.stdout.write('>')
		
		# Get the user input
		user_input = raw_input ()
		
		# Handle the user input
		# 	Built-in functions are executed
		#	Anything else are treated as searches
		if (not handleBuiltIn (user_input)): 
			searchAndOpen (user_input)
		
monster_list = []	# List of monster names that we have available
main()
