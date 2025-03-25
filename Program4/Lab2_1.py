import sys

def main():
    file1 = sys.argv[1]

    try:
        list1=read_file(file1)
        search=input('Enter a name to search for: ')            
    except FileNotFoundError as error:
        print(f"Error: The file '{file1}' could not be found.")
    else:
        for i in range (len(list1)):
            name=list1[i][0]
            if name == search:
                message=list1[i][1]
                display_entry(name,message)
        # for car in list1: 
        #     name=car[0]
        #     if name == search:
        #         message=car[1]
        #         display_entry(name,message)
            
                 
def read_file(filename):
    
    list1=[]
    list_of_tuples=[]
    with open (filename, 'r') as file1:
        name=file1.readline()
        while name !='':
            name=name.rstrip('\n')
            message=file1.readline()
            message=message.rstrip('\n')
            list1=tuple([name]+ [message])
            list_of_tuples.append(list1)
            name=file1.readline()
    return list_of_tuples       
    
        
def display_entry(name, message):
    print(f'[{name}] --> {message}')
    
        
if __name__ == '__main__':
    main()        