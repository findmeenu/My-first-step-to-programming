import sys

def read_file(filename):
    result_list=[]
    
    with open ((filename), 'r') as file_1:
        read_line=file_1.readline()
        while read_line !='':
            read_line=read_line.rstrip('\n')
            numbers=[int(num) for num in read_line.split()]
            read_line=file_1.readline()
            result_list+=numbers
    return result_list

def filter_odd_or_even (list1, keep_odd):
    odd=[]
    even=[]
    for value in list1:
        if (value)%2 ==0:
            value=[value]
            even+=value
            
        else:
            value=[value]
            odd+=value
    if keep_odd==True:
        return odd
    else:   
        return even
    
def reversed_bubble_sort(combined_list):
    count = len(combined_list)
    for j in range(count+1):
        for i in range(count-1):
            if combined_list[i] < combined_list[i+1]:
                combined_list[i], combined_list[i+1] = combined_list[i+1], combined_list[i]
    return combined_list
    
    # print(combined_list)

def main():
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    

#  with open (file1, 'r') as filename:
    list1=read_file(file1)  
    # print(list1)
    # with open (file2, 'r') as filename:
    list2=read_file(file2)
    # print(list2)
    odd_list=filter_odd_or_even(list1=list1, keep_odd=True)
    even_list=filter_odd_or_even(list1=list2, keep_odd=False)
    # print(odd_list)
    # print(even_list)
    combined_list=  odd_list + even_list
    # print(combined_list)
    
    reversed_bubble_sort(combined_list)
    print(combined_list)
    
if __name__== '__main__':    
    main()