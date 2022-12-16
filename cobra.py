# python3
# youtube demo: https://youtu.be/vA1irQxPzro
# Program name: cobra.py
# This is a C command line interpreter running in python
# CODER: Mike Root
# DATE: Nov. 21, 2022
# PURPOSE: Interactive C console simulator. User enters C commands which are compiled and run automatically.
#	   Users can list and select lines from a running history
# TO DO IMPROVE: Add file LOAD option
# Source cobra graphic: http://www.ascii-art.de/ascii/c/cobra.txt
# Note: This was built on Linux, so if you want to run on Windows you have to change some system calls eg:
#       os.sytem("clear") would become os.system("cls") to clear the screen

import os

# Name of file where the final output program will be stored
WORKING_FILE = "output.c"

# string to store currently loaded commands; meaning, commands that will run when user enters "go"
user_commands = ""

# historical list of all commands entered since beginning of program
command_history = ""


### Some functions for colour effects
def red():
	os.system('echo -n "\e[0;31m"')

def blue():
	os.system('echo -n "\e[0;34m"')

def reset_color():
	os.system('echo -n "\e[0m"')


### Simple graphic function
def show_cobra():
	# sweet ASCII cobra
	os.system("clear");
	red()

	print("""
         ,,'6''-,.
        <====,.;;--.
        _`---===. \"\"\"==__
      //\"\"@@-\\===\\@@@@ \"\"\\\\
     |( @@@  |===|  @@@  ||
      \\\\ @@   |===|  @@  //
        \\\\ @@ |===|@@@ //
         \\\\  |===|  //
___________\\\\|===| //_____,----\"\"\"\"\"\"\"\"\"\"-----,_
  \"\"\"\"---,__`\\===`/ _________,---------,____    `,
             |==||                           `\   \\
            |==| |          pb                 )   |
           |==| |       _____         ______,--'   '
           |=|  `----\"\"\"     `\"\"\"\"\"\"\"\"         _,-'
            `=\\     __,---\"\"\"-------------\"\"\"''
                \"\"\"\"""")

	reset_color()


# Introduce program to user
red()
print(  "______________________________________________________")
reset_color()
print("\n[Cobra]           cobra.py C Dojo            [Command]")
red()
print("\n type 'help' for options or 'cobra' to see cool cobra")
print("______________________________________________________")
reset_color()


# Setup C header and main function for output program
COMMANDO = """
#include <stdio.h>
#include <string.h>

int main()
{
	printf("\\e[0;31m--------------------------------------------------\\e[0m\\n");

"""

# Continuous user input loop waits for user commands
while True:
	# wait for and retrieve user input
	comm = input("<cobra>   ")

	# save, compile, and run the code currently stored in user_commands string
	if comm == "go":
		# magic happens
		with open(WORKING_FILE, "w") as f:
			f.write(COMMANDO + user_commands +
				"printf(\"\\n\\e[0;31m--------------------------------------------------\\e[0m\\n\"); return 0;}")
		os.system("gcc " + WORKING_FILE + "; ./a.out")

	# if just newline all alone, then ignore
	elif len(comm) == 0:
		continue

	# basic help menu for helping
	elif comm == "help":
		red()
		print("_______________________________________________________________________________________")
		reset_color()
		print("""
	Just enter C commands as you normally would in a C main() function
	for example:	int a = 7; printf("%d\\n", a); // will print 7
	Commands will be stored and then run in main() function of program: """ + WORKING_FILE + """

	COMMAND		DESCRIPTION

	go		Run currently loaded lines of code
	clear		Clear loaded code
	show		Show loaded code that is ready to run
	hist		History: lists all commands entered since starting program
	!n n n...	Appends history commands to loaded command list;
			for example, use:   !2 3 4   to load history lines 2, 3, and 4
			Also overwrites existing history with selected lines
	-n1 n2		Select lines n1 to n2 inclusive from history (hist);
			also overwrites existing history with selected lines
	quit		Quit console
	cls		Clear screen
	cobra		Show scary cobra""")
		red()
		print("_______________________________________________________________________________________\n")
		reset_color()


	# You want to see a cobra?
	elif comm == "cobra":
		show_cobra()

	# Exit the program
	elif comm == "quit":
		print("[+] Ok computer")
		# break out of the interactive loop
		break

	# Clear loaded user commands
	elif comm == "clear":
		user_commands = ""

	# Show loaded user commands
	elif comm == "show":
		# print("\n" + user_commands)
		L = user_commands.split("\n")
		for i in range(len(L) - 1):
			print(str(i) + "\t" + L[i])
		print("")

	# Print command history
	elif comm == "hist":
		# print("\n" + user_commands)
		L = command_history.split("\n")
		for i in range(len(L) - 1):
			print(str(i) + "\t" + L[i])
		print("")

	# Select commands from history
	elif comm[0] == "!":
		comm_choices = comm[1:].split(" ")
		H = command_history.split("\n")
		for n in comm_choices:
			user_commands += H[int(n)] + "\n"
		command_history = user_commands

	# Select line range from history
	elif comm[0] == "-":
		C = comm[1:].split(" ")[0:2]
		st = int(C[0])
		fn = int(C[1])
		print(str(st) + " " + str(fn))
		H = command_history.split("\n")
		for n in range(st, (fn + 1)):
			user_commands += H[int(n)] + "\n"
		command_history = user_commands

	# Clear the screen
	elif comm == "cls":
		os.system("clear")

	# Else we assume user input is a C command
	else:
		user_commands += (comm + "\n")
		command_history += (comm + "\n")

# End of program
