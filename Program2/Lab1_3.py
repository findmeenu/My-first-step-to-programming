print('Welcome to the Money Bag Transport Calculator (M.B.T.C)')
print("-------------------------------------------------------")
print()

big_bag_size = 80
medium_bag_size = 50
small_bag_size = 20

big_bag_worth = 60000
medium_bag_worth = 30000
small_bag_worth = 10000

truck_size=int(input('What is the volume of the truck (>=100): '))

while truck_size < 100:
    truck_size=int(input('What is the volume of the truck (>=100): '))
    
# No. of different size bags which can fit in truck

no_of_big_bags = (truck_size//big_bag_size)
big_bag_worth *= no_of_big_bags
remaining_space =truck_size-(no_of_big_bags*big_bag_size)

# print(remaining_space)
no_of_medium_bags = (remaining_space//medium_bag_size)
medium_bag_worth *= no_of_medium_bags
remaining_space -= (no_of_medium_bags*medium_bag_size)
# print(remaining_space)
no_of_small_bags = (remaining_space//small_bag_size)
small_bag_worth *= no_of_small_bags
remaining_space -=(no_of_small_bags*small_bag_size)
# print(remaining_space)


total_value = big_bag_worth+medium_bag_worth+small_bag_worth

print()
print('Packing Plan')
print('------------')
print(f"{no_of_big_bags:<2}big bags")
print(f"{no_of_medium_bags:<2}medium bags")
print(f"{no_of_small_bags:<2}small bags")
print()
print(f"{'Space left ':<11}: {remaining_space}{'L':<} ")
print(f"{'Total value':<11}: {total_value}{'kr':<}")
print()
 
    

    
    
