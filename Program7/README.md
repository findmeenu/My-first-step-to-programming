Task description
A lot of police investigations start off by examining where the potential suspects were at the time of the crime. This is often done by asking phone companies to provide lists of all mobile phones that were in the area where the crime was committed around the time when it was committed. If there is only one crime scene this is not a big problem but if there are several crime scenes then the task of cross referencing the lists gets quite tedious. To combat this the local police department has decided to automate the process by creating a script that automatically does most of the work for them.

The script shall work as follows:

(Step 1) Start the script
(Step 2) Provide one or more paths to files with phone numbers
(Step 3) The script finds out what phone numbers occur in all files
(Step 4) The script looks up who owns the phone numbers found
(Step 5) The script displays the found names

 To break it all down a little bit further this is what should happen during each step. 

When starting the script, a path to a file that contains the mapping between name and number shall be given as a command line argument. This file shall contain a pickled dictionary on the following format {‘0709-12345’: ‘Anna Karlsson’}.
To be able to provide an arbitrary number of files a menu is needed. The menu shall have the following options: 1. Add file and 2. Calculate. All file paths added shall be saved in a list for later use.
This step is part of the menu option 2. Calculate. The script shall cross reference the numbers in all the files provided and create a Set with the ones that occur in all files. The files with the phone numbers store one phone number per line and is saved as a regular text file.
This step is part of the menu option 2. Calculate. Using the Set of found numbers the script looks up the owner’s names using the file sent as a command line argument. The names shall be saved in a list.
All the found names located in the set from Step 4 is displayed on the screen.
The student must implement the following functions:

display_menu()
This function shall display the following menu on screen:

1. Add file
2. Calculate
 cross_reference(files)
The parameter files shall be a list of filenames (full path). The files shall be files containing one phone number per line. The function shall create, and return, a Set containing all the phone numbers that occurs in all files. If given an invalid filename the function shall raise a FileNotFoundException (do not have a try-except in this function).

 map_numbers_to_names(numbers, filename)
This function shall match each number from the Set numbers to a name and store the names in a list. To accomplish this, the function shall use a dictionary that is loaded (using pickle) from the file filename. The dictionary shall use the format {‘0709-12345’: ‘Anna Karlsson’}. If a number can not be found in the dictionary it shall be listed as Unknown with the phone number attached, like can be seen in this example: Unknown (0709-11111). The function shall return the list with the names and/or unknown tags. If given an invalid filename the function shall raise a FileNotFoundException (do not have a try-except in this function).

display_suspects(names)
As the name of the function suggests this function shall display the names of all suspects sent to the function as a list of strings. The format shall be exactly as shown here:

The following persons was present on all crime scenes:
------------------------------------------------------
Max Olsson
Zara Walthersson
Unknown (0703-23464)
If the list sent as a parameter is empty the following message shall be shown:

The following persons was present on all crime scenes:
------------------------------------------------------
No matches
main()
This function shall have a loop that displayed the menu and handles the user input. Depending on the input from the user the function shall either read more filenames or try to find the suspects and print their names using the file from the command line argument for the mapping between numbers and names. Besides having the "main loop" this function shall also be responsible for the error handling in the script and print the error message below if the file given as command line arguments or the files specified while running the script are not valid: 

Error: There was a problem with at least one of the files.
 

To avoid problems with the testing framework, and to build a good habit, call the main function using the following construct:

if __name__ == '__main__':
    main()
 

Comments and additional resources   

Students are highly recommended to first solve all the tasks from the corresponding lectures and exercises before attempting to solve this problem. Having a solid plan before starting to code will also help
The student can upload as many times as he or she likes to before the deadline
The file owners Download ownerscan be used as an example of a file mapping owners to phone numbers
These files can be used as examples of how the list of phone numbers from a crime scenes will look like:
crime scene 1Links to an external site. 
crime scene 2Links to an external site. 
crime scene 3Links to an external site.  
This videoLinks to an external site. covers how to use command line arguments and why we call main the way we do
This videoLinks to an external site. shows what the script shall look like and how it shall work when finished
