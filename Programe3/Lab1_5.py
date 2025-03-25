option=''
sub_option='0'

monday_purchase=0
monday_repurchase=0
tuesday_purchase=0
tuesday_repurchase=0
wednesday_purchase=0
wednesday_repurchase=0
thursday_purchase=0
thursday_repurchase=0
friday_purchase=0
friday_repurchase=0
monday_sales= monday_purchase-monday_repurchase
tuesday_sales= tuesday_purchase-tuesday_repurchase
wednesday_sales= wednesday_purchase-wednesday_repurchase
thursday_sales= thursday_purchase-thursday_repurchase
friday_sales= friday_purchase-friday_repurchase
total_sales=monday_sales+tuesday_sales+wednesday_sales+thursday_sales+friday_sales
# monday_avg_sales = monday_sales/total_sales
# tuesday_avg_sales = tuesday_sales/total_sales
# wednesday_avg_sales = wednesday_sales/total_sales
# thursday_avg_sales = thursday_sales/total_sales
# friday_avg_sales = friday_sales/total_sales
    
                    
while option == '': #or sub_option== '0':#or sub_option> 5 or sub_option_re<1 or sub_option_re>5 or sub_option == 'B' or sub_option_re =='B' :
    print("*----------------------------------------*")
    print(f"|{'Main Menu':^40}|")
    print("*----------------------------------------*")
    print(f"|{'Option':^8}|{'Description':^31}|")
    print("*----------------------------------------*")
    print(f"|{'1':^8}|{' Register Purchase':<31}|")
    print(f"|{'2':^8}|{' Register Reurchase':<31}|")
    print(f"|{'3':^8}|{' Earnings (Amount per day)':<31}|")
    print(f"|{'4':^8}|{' Earnings (Percentage per day)':<31}|")
    print(f"|{'E':^8}|{' EXIT':<31}|")
    print("*----------------------------------------*")
    option=(input('Enter your option >> '))
    print()
    
    if (option <'0' and option!='E') or (option >'4' and option!='E'):
        print('Error: Not a valid option!')
        option=''
        # if (option <'0' and option!='E') or (option >'4' and option!='E'):
        
            
 # Second while inner loop as we want to execute main menu again if sub_option is invalid data.           
    if option =='1':
        print("*----------------------*")
        print(f"|{'Purchase':^22}|")
        print("*----------------------*")
        print(f"|{'Option':^8}|{'Description':^13}|")
        print("*----------------------*")
        print(f"|{'1':^8}|{'Monday':<13}|")
        print(f"|{'2':^8}|{'Tuesday':<13}|")
        print(f"|{'3':^8}|{'Wednesday':<13}|")
        print(f"|{'4':^8}|{'Thursday':<13}|")
        print(f"|{'5':^8}|{'Friday':<13}|")
        print(f"|{'B':^8}|{'Go back':<13}|")
        print("*----------------------*")
        sub_option=input('Enter your option >> ')
        print()
        if (sub_option <= '0' and sub_option !='B') or (sub_option>'5' and sub_option !='B'):
            print('Error: Not a valid option!')
            option=''
        elif sub_option >='1' and sub_option <='5':
                purchase=int(input('Enter purchase sum >> '))
                print()
        
        if sub_option=='1':
            monday_purchase += purchase
            option=''
        elif sub_option=='2':
            tuesday_purchase += purchase
            option=''
        elif sub_option=='3':
            wednesday_purchase += purchase
            option=''
        elif sub_option=='4':
            thursday_purchase += purchase
            option=''
        elif sub_option=='5':
            friday_purchase += purchase
            option=''
        elif sub_option == 'B' :
            option=''
                
# 3rd while loop for sub_option as we want to execute main menu again if sub_option is invalid data.     
           
    while option =='2':
        print("*----------------------*")
        print(f"|{'Repurchase':^22}|")
        print("*----------------------*")
        print(f"|{'Option':^8}|{'Description':^13}|")
        print("*----------------------*")
        print(f"|{'1':^8}|{'Monday':<13}|")
        print(f"|{'2':^8}|{'Tuesday':<13}|")
        print(f"|{'3':^8}|{'Wednesday':<13}|")
        print(f"|{'4':^8}|{'Thursday':<13}|")
        print(f"|{'5':^8}|{'Friday':<13}|")
        print(f"|{'B':^8}|{'Go back':<13}|")
        print("*----------------------*")
        sub_option=input('Enter your option >> ')
        print()
        if (sub_option <= '0' and sub_option !='B') or (sub_option>'5' and sub_option !='B'):
            print('Error: Not a valid option!')
            option=''
        elif sub_option >='1' and sub_option <='5':
            repurchase=-int(input('Enter repurchase sum >> '))
            print()
        if sub_option=='1':
            monday_repurchase -= repurchase
            option=''
        elif sub_option=='2':
            tuesday_repurchase -= repurchase
            option=''
        elif sub_option=='3':
            wednesday_repurchase -= repurchase
            option=''
        elif sub_option=='4':
            thursday_repurchase -= repurchase
            option=''
        elif sub_option=='5':
            friday_repurchase -= repurchase
            option=''
        elif sub_option =='B':
            option=''
            
            
# Earnings per day

    while option == '3':
        print()
        monday_sales= monday_purchase-monday_repurchase
        tuesday_sales= tuesday_purchase-tuesday_repurchase
        wednesday_sales= wednesday_purchase-wednesday_repurchase
        thursday_sales= thursday_purchase-thursday_repurchase
        friday_sales= friday_purchase-friday_repurchase
        # or tuesday_sales<0 or wednesday_sales<0 or thursday_sales<0 or friday_sales<0:
        if monday_sales<0: 
            print(f"{'Monday':<10}:{monday_sales:>11}kr (LOSS)")
        else: #monday_sales>=0:
            print(f"{'Monday':<10}:{monday_sales:>11}kr")
            
        if tuesday_sales<0:
            print(f"{'Tuesday':<10}:{tuesday_sales:>11}kr (LOSS)")
        else:
            print(f"{'Tuesday':<10}:{tuesday_sales:>11}kr")
            
        if wednesday_sales<0:
            print(f"{'Wednesday':<10}:{wednesday_sales:>11}kr (LOSS)")
        else:
            print(f"{'Wednesday':<10}:{wednesday_sales:>11}kr")
            
        if thursday_sales<0:
            print(f"{'Thursday':<10}:{thursday_sales:>11}kr (LOSS)")
        else:
            print(f"{'Thursday':<10}:{thursday_sales:>11}kr")
            
        if friday_sales<0:
            print(f"{'Friday':<10}:{friday_sales:>11}kr (LOSS)")
        else:
            print(f"{'Friday':<10}:{friday_sales:>11}kr")
            
        option=''
        
   
    if option==4:
        print(total_sales)
        # monday_avg_sales = monday_sales/total_sales
        # print(monday_avg_sales)
        # print(f"{'Monday':<10}:{(monday_sales/total_sales):>11.1f}%")
        # print(f"{'Tuesday':<10}:{(tuesday_sales/total_sales):>11.1f}%")
        # # print(f"{'Wednesday':<10}:{wednesday_avg_sales:>11.1f}%")
        # print(f"{'Thursday':<10}:{thursday_avg_sales:>11.1f}%")
        # print(f"{'Friday':<10}:{friday_avg_sales:>11.1f}%")
                
                    
    if option=='E':
        break   
    
