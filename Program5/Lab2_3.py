import sys

def read_lines(filename):
    car_list = []
    with open(filename, 'r') as car_data:
            car_name=car_data.readline()
            while car_name != '':
                car_name=car_name.rstrip('\n')
                car_list.append(car_name)
                car_name=car_data.readline()
    return car_list


def parse_cars(car_list):
    i=0
    car_new_list=[]
    while i < len(car_list):
        car_name=car_list[i]
        car_name2=car_name.split(':')
        car_name=tuple([car_name2[0]] +[int(car_name2[1])])   #concatenate the list & convert it to tuple.as input was list.
        # car_range_num=[int(car_name2[1])]
        i+=1
        # tuple_list=tuple(car_name)
        car_new_list.append(car_name)
    return car_new_list        

def calculate_percentage(distance, car_tuple_list):
    i=0
    car_percent_list=[]
    while i < len(car_tuple_list):
        percentage=car_tuple_list[i][1]
                        # percentage=percentage[1]
        cal_per=(f'{(distance/percentage)*100}')
        car_per_tuple=tuple([car_tuple_list[i][0]] + [float(cal_per)])  #concatenate the list & convert it to tuple.as input w
        car_percent_list.append(car_per_tuple)
        i+=1
    return car_percent_list

def display_result(car_percent_list):
    print(f'To drive the specified distance would correspond to this many\npercent of each cars specified max range.')
    i=0
    while i< len(car_percent_list):
        if car_percent_list[i][1] <= 100.0: 
            print(f'{car_percent_list[i][0]:<37}-->  {car_percent_list[i][1]:>.0f}%')
        else:
            print(f'{car_percent_list[i][0]:<37}-->  Distance exceeds max range ({car_percent_list[i][1]:>.0f}%)')
        i+=1    


def main():
    
    file1 = sys.argv[1]
    
    try:
        list1=read_lines(file1)
        distance=int(input('How far do you want to drive (kilometers)? '))
    except FileNotFoundError as a:
        print('An error occurred while trying to read the file.')
    else:
        car_tuple_list= parse_cars(list1)
        car_percent_list=calculate_percentage(distance,car_tuple_list)
        display_result(car_percent_list)


if __name__== '__main__':    
    main()