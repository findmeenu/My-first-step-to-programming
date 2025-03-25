import pickle
import sys

def display_menu():
    print()
    print('1. Add file (Enter a for 1 & b for 2)')
    print('2. Calculate (Enter a for 1 & b for 2)')
    print()
    
def cross_reference(files_list):
    sets=[]
    for files in files_list:
        with open(files, 'r') as file:
            data = file.read().splitlines()
            new_set = set(data)
            sets.append(new_set)
    if len(sets)>0:
        intersection=sets[0]
        for i in range (1, len(sets)):
            intersection=intersection.intersection(sets[i])
            
    else:
        intersection=set()
        
    return intersection

def display_suspects(names):
    print()
    print('The following persons was present on all crime scenes:')
    print('------------------------------------------------------')
    if len(names) == 0:
        print("No matches")
    else:
        for item in names:
            print(item)
            
def map_numbers_to_names(numbers, filename):
    intersection_list=[]
    with open (filename, 'rb') as owners:
        a=pickle.load(owners)
        for items in numbers:
            name=a.get(items, 'Unknown')
            if name != 'Unknown':
                intersection_list.append(name)
            else:
                name='Unknown ' + '(' + items + ')' 
                intersection_list.append(name)
    return intersection_list
            
def main():
    try:
        
        filename=sys.argv [1]
        my_list=[]
        choice=''
        while choice =='':
            display_menu()
            choice=(input('Enter choice: '))
            if choice!= '1' and choice != '2':
                choice=''
            elif choice== '1':
                files=input('Enter a filename (include full path): ')
                my_list.append(files)
                choice=''
            else :
                numbers=cross_reference(my_list)
                x_marked=map_numbers_to_names(numbers, filename)
                display_suspects(x_marked)  
                   
    except (FileNotFoundError, KeyError) as err  :
        print()
        print('Error: There was a problem with at least one of the files.')
        
    
if __name__=='__main__':
    main()