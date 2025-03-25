
print('Ticket types: ')
print(f"1. {'Budget':<10}({'500Kr':>6})")
print(f"2. {'Economy':<10}({'750Kr':>6})")
print(f"3. {'VIP':<10}({'2000Kr':>6})")

no_of_bags=0
no_of_meals=0
bag=200
meal=150

price_of_economy_ticket =750
price_of_budget_ticket =500
price_of_VIP_ticket =2000

total=0

ticket_type = int(input('Specify the ticket (using 1,2 or 3) : '))

while ticket_type < 1 or ticket_type >3:
    ticket_type = int(input('Specify the ticket (using 1,2 or 3) : '))
    
    
if ticket_type == 1:
    total+=price_of_budget_ticket
elif ticket_type == 2:

    total+= price_of_economy_ticket
elif ticket_type == 3:
        
    total+= price_of_VIP_ticket     
        
 


option = 1

while option >0 and option<5:
    print(f"\nCurrently you have: \n    {no_of_bags} bag(s) registered \n    {no_of_meals} meal(s) registered")
    print("\nHere are your options): ")
    print("1. Add bag (max 1)")
    print("2. Add meal (max 1)")
    print("3. Remove bag")
    print("4. Remove meal")
    print("5. Fianlize ticket")
    option = int(input('Your choice >> '))
    
    while option <1 or option >5:
        option = int(input('Your choice >> '))
        
    if option == 1:
        if no_of_bags ==0:
            no_of_bags+=1

    elif option ==2:
        if no_of_meals==0:
            no_of_meals+=1
        
    elif option == 3:
        if no_of_bags==1:
            no_of_bags-=1
        
    elif option == 4:
        if no_of_meals>0:
            no_of_meals-=1


print('Receipt:')
print(f"{'Ticket':<7}:{total:>5}kr")

if no_of_bags>0:
    bag=(bag)*(no_of_bags)
    total=total+bag
    print(f"{'Bag':<7}:{bag:>5}kr")
    
if no_of_meals>0:
    meal*=no_of_meals
    total=total+meal
    print(f"{'Meal':<7}:{meal:>5}kr")

print(f"{'':<7} {'-------':>5}")
print(f"{'Total':<7}:{total:>5}kr")
print()
