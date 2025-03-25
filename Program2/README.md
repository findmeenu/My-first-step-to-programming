Requirements

The script must pass all the automatic tests and a manual inspection
The problem must be solved individually, without help from others and/or use of AI-tools
Any suspicion about cheating, cooperation, and/or plagiarism will be reported to the Discipline Board
The students script will be checked both manually and using anti-plagiarism software
 

Instructions

Analyse the problem below using Polya's Problem solving TechniqueLinks to an external site.
Create a script named Lab1_3.py that solves the problem according to the given instructions
Pay special attention when formatting the output as it must match the specified format exactly (character by character) to pass the tests 
Upload the script using the link below
 

Task description
A local bank office often transports bags of money to and from their main office. They have asked you to develop a script that can help them know beforehand how many bags will fit in the truck transporting the money, and what the value of all the bags combined is.

The truck transporting the money bags can vary in size from transport to transport so the size must be read from the user each time running the script. If the user enters a volume less than 100L they shall be asked again until they give a volume larger than, or equal to, 100L.

After having read the size of the truck, the script shall calculate how many money bags of each size fits in the specified truck and display it on exactly the following format:

2 big bags
1 medium bags 
0 small bags
 The banks internal policy documents dictate that they must only use bags in three sizes (20L, 50L, and 80L) and that they must always use as many of the bigger bags as possible. Here is an example to illustrate this:

Truck size = 220L 

1. How many big bags (80L) can we fit in 220L? Answer is 2. 
   We now have 60L left in truck.

2. How many medium bags (50L) can we fit in the remaining 60L? Answer is 1. 
   There is still 10L left in the truck.

3. How many small bags (20L) can we fit in the remaining 10L? Answer is 0. 
   There is 10L left in the truck that we can not fit any bag into. 
Having decided how many bags can be transported it is time to calculate the remaining space in the truck and how much the shipment is worth. A small bag is worth 10000kr, a medium bag 30000kr, and a big bag is worth 60000kr. Finally we want to display this information to the user using the following format:

Space left : 10L
Total value: 150000kr
 

Comments and additional resources

Students are highly recommended to first solve all the tasks from the corresponding lectures and exercises before attempting to solve this problem. Having a solid plan before starting to code will also help
The student can upload as many times as he or she likes to before the deadline
Do not use the tab character (\t) to align the output
When it comes to calculating how many bags of each size one will end up with the student has different options, either to use loops or to use math. If the student opts for using loops it might help to imagine adding one bag at the time to the truck, first as many big bags as possible, then as many medium bags as possible, and finally as many small bags as possible
This videoLinks to an external site. shows what the script shall look like and how it shall work when finished
 


