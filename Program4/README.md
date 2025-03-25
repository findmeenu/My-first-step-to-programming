Requirements

The script must pass all the automatic tests and a manual inspection
The problem must be solved individually, without help from others and/or use of AI-tools
Any suspicion about cheating, cooperation, and/or plagiarism will be reported to the Discipline Board
The students script will be checked both manually and using anti-plagiarism software
 

Instructions:

Analyse the problem below using Polya's Problem solving TechniqueLinks to an external site.
Create a script named Lab2_1.py that solves the problem according to the given instructions
Pay special attention when formatting the output as it must match the specified format exactly (character by character) to pass the tests 
Upload the script using the link below
 

Task description:

With this new work from home situation your small team of developers has quickly found out how much questions you used to ask each other in person. Now that you all work from home most of the time you have resorted to using online chat instead. But this has resulted in that you all have to go back and read endless chat logs when you forget what you agreed on earlier.

To remedy this problem, you have decided to write a small script that reads a log file and then allow you to search for all messages sent by one user. To make the script a bit more versatile you have decided that the path to the log file shall be sent as a command line argument to the script. As everyone in the team is a bit sloppy when typing, the script needs to have error handling that clearly informs the user in case the specified path to the log file does not exist.

The script shall have a main function, a function for reading from the log file, and a function for formatting and displaying a message on the screen. Here are some rules for how each of the functions shall work:

read_file(filename):

Shall read the file specified by the parameter filename and create a list of tuples that is then returned. Each tuple shall consist of a name and a message. In the file, each message takes up two rows, where the first row contains the senders name, and the second row contains the text of the message. Each log file can of course contain many messages sent by many different persons. If the filename parameter is not a valid path, the function shall raise an FileNotFoundError (do not have a try-except in this function).

display_entry(name, message)
Shall use the two parameters to display a formatted output on the screen. The output shall follow this format exactly:

[name] --> message
main()
This function shall read the command line argument, ask what name to search the log file for, and use the other functions as needed to display all messages send by the specified name. This function shall also handle the FileNotFoundErrors raised by the read_file function. Should an error occur, show an error message on the following format:

Error: The file '/Users/nna/messages.txt' could not be found.
 

To avoid problems with the testing framework, and to build a good habit, call the main function using the following construct:

if __name__ == '__main__':
    main()
 

Comments and additional resources   

Students are highly recommended to first solve all the tasks from the corresponding lectures and exercises before attempting to solve this problem. Having a solid plan before starting to code will also help
The student can upload as many times as he or she likes to before the deadline
Do not use the tab character (\t) to align the output
An example log file can be found hereLinks to an external site.
This videoLinks to an external site. covers how to use command line arguments and why we call main the way we do
This videoLinks to an external site. shows what the script shall look like and how it shall work when finished
