temp="" #set initial value
while temp != "exit":
    temp=input('Enter the temperature and Celsius or Fahrenheit, or type Exit: ')
    temp_sep=temp.split()
    #str.isnumeric() returns True if all characters in string are numeric and there is at least one character.
    if len(temp_sep)==2 and temp_sep[0].isalpha()==False:
        temp_num=float(temp_sep[0])
        temp_unit=temp_sep[1]
        temp_unit=temp_unit.lower()
        if temp_unit=='celsius':
            temp_fah=(temp_num*1.8)+32
            temp_fah_round=round(temp_fah,2)
            print(temp_sep[0],'Celsius equals',temp_fah_round,'Fahrenheit.\n')
        elif temp_unit=='fahrenheit':
            temp_cels=(temp_num-32)/1.8
            temp_cels_round=round(temp_cels,2)
            print(temp_sep[0],'Fahrenheit equals',temp_cels_round,'Celsius.\n')
        elif temp_unit !='celsius' or temp_unit !='fahrenheit':
            print('Please specify "Celsisus" or "Fahrenheit". \n')
    else:
        if temp_sep[0].lower()=="exit":
           temp=temp_sep[0].lower()
           print("Goodbye.\n")
        elif len(temp_sep)==1 and temp_sep[0].isalpha()==False:
            print('Please specify "Celsisus" or "Fahrenheit". \n')
        else:
            print("I don't understand. Try again.\n")
