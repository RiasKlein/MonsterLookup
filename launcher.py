################################################################################
#
#	launcher.py
#	
#	Launcher for Monster Lookup. 
#
#	Program by Shunman Tse
#
################################################################################

import os, sys, webbrowser
from Modules.listToHTML import listToHTML

# Configurable Global Settings
file_monster_list = 'monster_list.txt'			# file with the monster HTML file names
html_monster_list_fname = 'monster_list.html'
html_monster_list_header = "Monster List"
system_version = '0.2'
system_title = 'Dungeons and Dragons 5e Monster Lookup'

monster_list = []			# List of default monster names
custom_monster_list = []	# List of custom monsters

# readMonsterList
#	Function reads the file monster_list.txt for all currently available monsters
#	Each entry is added into the list called monster_list
def readMonsterList ():
	# List of monster names
	list = []

	# Open 'monster_list.txt' in reading mode
	rfile = open (file_monster_list, 'r')
	
	# We'll keep going until we reach the end of the file
	while True:
		line = rfile.readline()		# Get a line from 'monster_list.txt'
		if not line: 
			rfile.close()			# Close the file now that we are done
			return list				# End the function if we're at the end

		# Only add .html files because those contain the monster files
		if ('.html' in line):
			line = line.rstrip ('\n')			# Remove the trailing new line
			line = line[:-5]					# Get rid of the .html
			list.append (line.lower())	# Append as entry into the list of monsters

# helpReadme
#	Print system version and provides a program description.			
def helpReadme ():
	# Print out the current version
	print ("System Version: " + system_version)
	
	# Now for a program description
	print ("""
Monster Lookup is a collection of D&D monster statblocks. 
To view a monster statblock, enter the name of the monster of interest and then press ENTER. 
The system has been tested with using lowercase monster names. 	
The list of available monsters should have opened on a new browser tab.""")

# handleBuiltIn
#	Function handles the built-in functions	
#	Returns whether the provided input is a built-in function	
def handleBuiltIn ( user_input ):
	is_builtin = False

	# If the input was 'help', then provide the available monster list
	if (user_input.lower() == 'help'):
		is_builtin = True

		os.chdir ('./Monsters')
		webbrowser.open_new_tab (html_monster_list_fname)	# Open the HTML file with the monster names
		os.chdir ('..')	
		
		os.chdir ('./Custom Monsters')
		webbrowser.open_new_tab (html_monster_list_fname)	# Open the HTML file with the monster names
		os.chdir ('..')	
		
		helpReadme()
		
	# If the input was an empty string, then do nothing
	elif (user_input.lower() == ""):
		return True
		
	# If the input was 'exit', then exit the system
	elif (user_input.lower() == 'exit'):
		print ("Exiting...")
		
		# Cleanup generated file in Monsters folder
		os.chdir ('./Monsters')					# Change to the Monsters directory
		os.remove (html_monster_list_fname)		# Remove the file
		os.chdir ('..')							# Back out to the main directory
		
		# Cleanup generated file in Custom Monsters folder
		os.chdir ('./Custom Monsters')			# Change into the Custom Monsters directory
		os.remove (html_monster_list_fname)		# Remove the file
		os.chdir ('..')							# Back out to the main directory
		
		sys.exit()
		
	return is_builtin

# searchAndOpen
#	Function opens the monster file for the monster if it exists
#	Feedback is given regardless
def searchAndOpen ( user_input ):
	# Check for the monster name in the default monster list
	if user_input.lower() in monster_list:
		os.chdir ('./Monsters')			# Go to the Monsters directory
		name = user_input + '.html'		# Make the filename for the monster input
		webbrowser.open_new_tab (name)	# Open the file in the browser
		os.chdir ('..')					# Back up to the main directory
		
	# Check for the monster name in the custom monster list
	elif user_input.lower() in custom_monster_list:
		os.chdir ('./Custom Monsters')	# Go to the Custom Monsters directory
		name = user_input + '.html'		# Make the filename for the monster input
		webbrowser.open_new_tab (name)	# Open the file in the browser
		os.chdir ('..')					# Back up to the main directory
		
	else:
		# If the monster name was not found, then give output saying so
		print ("Monster Not Found")

# printIntroduction
#	Function prints out basic information displayed at the start		
def printIntroduction ():
	system_title_buffer = 20
	print ("=" * (2 * system_title_buffer + len(system_title)) + "\n" + " " * system_title_buffer + system_title + "\n" + "=" * (2 * system_title_buffer + len(system_title)))
	print ("Type in a monster name to look for or type in 'help' for more information")
	
# initialize
#	Change program title and load in monster names	
def initialize ():
	# Setting the title for the program
	os.system ("title " + system_title)
	
	# Read in the names of all default monsters
	global monster_list					# We want to change the global monster_list
	os.chdir ('./Monsters')				# Change the working directory to the Monsters folder
	monster_list = readMonsterList()	# Get the names of all available monsters (default list)
	# Create an updated HTML file to display all the available monsters
	listToHTML ( file_monster_list, html_monster_list_fname, html_monster_list_header)
	os.chdir ('..')						# Back up to the main folder
	
	# Read in the names of all custom monsters
	global custom_monster_list			# We want to change the global custom_monster_list
	os.chdir ('./Custom Monsters')		# Change the working directory to the Custom Monsters folder
	custom_monster_list = readMonsterList()	# Get the names of all available custom creatures
	listToHTML ( file_monster_list, html_monster_list_fname, "Custom Monster List")
	os.chdir ('..')						# Back up to the main folder
	
	# Introduction Information!
	printIntroduction ()
		
def main():
	initialize ()	
	
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

main()
