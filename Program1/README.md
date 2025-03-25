# My-first-step-to-programming
My first step into world of programming.


Task Requirements

The script must pass all the automatic tests and a manual inspection
The problem must be solved individually, without help from others and/or use of AI-tools
Any suspicion about cheating, cooperation, and/or plagiarism will be reported to the Discipline Board
The students script will be checked both manually and using anti-plagiarism software
 

Instructions

Analyse the problem below using Polya's Problem solving TechniqueLinks to an external site.
Create a script named Lab1_1.py that solves the problem according to the given instructions
Pay special attention when formatting the output as it must match the specified format exactly (character by character) to pass the tests 
Upload the script using the link below
 

Task description
A travel company needs you to develop a script that can help them decide the price of their tickets. The company want the script to work in accordance with the following three steps:

Chose a ticket type
The first thing the user of the script shall do is to select a ticket type using a menu looking like this:

Ticket types:
1. Budget  ( 500kr)
2. Economy ( 750kr)
3. VIP     (2000kr)
 

Menu for optional purchases
Next, the user shall be presented with a menu where he or she can select what to include in the ticket. The user shall be able to add a bag (max 1) or a meal (max 1). The user shall also be able to remove already added bags or meals. Finally the user shall be able to finalize the ticket. Above the menu the script shall also display if a bag and/or meal has been selected. The company wants the menu to look like this:

Currently you have:
    0 bag(s) registered
    0 meal(s) registered

Here are your options:
1. Add bag (max 1)
2. Add meal (max 1)
3. Remove bag
4. Remove meal
5. Finalize ticket
 

Finalizing the ticket
When the user selects to finalize the ticket the script shall calculate the price of the ticket and any optional purchases according to the following price list:

Budget ticket = 500kr

Economy ticket = 750kr

VIP = 2000kr

Bag included = 200kr

Meal included = 150kr

The travel company insists that the last output shall look like an actual receipt and they require it to formatted exactly as can be seen in the examples below. The Bag and/or Meal parts of the receipt shall only show up if they have been selected. 

Example of a receipt with a VIP ticket, a bag, and a meal:

Receipt:
Ticket : 2000kr
Bag    :  200kr
Meal   :  150kr
        -------
Total  : 2350kr
Example of a receipt with only a Budget ticket:

Receipt:
Ticket :  500kr
        -------
Total  :  500kr
 

Comments and additional resources   

Students are highly recommended to first solve all the tasks from the corresponding lectures and exercises before attempting to solve this problem. Having a solid plan before starting to code will also help
The student can upload as many times as he or she likes to before the deadline
Do not use the tab character (\t) to align the output
When placing a menu inside a loop like in this case, do not forget to add an option to exit the loop
Using one variable for each of the things we want to remember might be a good approach 
This videoLinks to an external site. shows what the script shall look like and how it shall work when finished
