# Monster Lookup System
This system provides dungeon masters with easy access to monster information; it should be useful during campaigns or during the campaign planning process.

## Using the System

* To start up the system, just double click on launcher.py or use the command **python launcher.py**
* The built-in commands for the system are: 'help' and 'exit'
  - help: prints out the version number of the system and a list of all available monster names 
  - exit: exits the system
* Just type in the name of the monster you are looking for and hit enter for the corresponding browser page to open up.

## Requirements
* Certain functionalities are only provided in Google Chrome. Make sure that Google Chrome is your default browser.
* You must have Python 2.7 installed. Go here for the download: https://www.python.org/downloads/
* The intended OS is Windows. Certain bugs may appear on UNIX systems.

## Adding Monsters to the System

* To add more monster stat pages to the system, you need to:
  - 1. Create a new HTML file for the monster. The naming convention for the new HTML file is: [name of the monster].html
  - 2. Add in the proper information for the new monster in the HTML file. 
  - 3. Update 'monster_list.txt' in the Monsters folder to include your new HTML file
* It is recommended that you copy & paste one of the existing monster files and make modifications for new entries.
* For Windows users, step 3 can be completed by using the command: **dir /b > monster_list.txt**

## The Future of the System

* More monster entries will be included over time.
* Basic generator utilities are now available to assist in the monster creation process. 
