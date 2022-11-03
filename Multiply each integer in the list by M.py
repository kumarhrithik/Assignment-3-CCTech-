'''Write a program to accept a list L1 of N integers. Accept integer M. 
   Multiply each integer in the list by M and generate a new list L2. Print the lists L1 and L2.'''

def get_multiplied_list(len_list, num_list, to_multiply):
    if int(len_list) == len(num_list) and to_multiply.isnumeric():
        try:
            new_num_list = [int(x) for x in num_list]
            multiplied_list = []
            for i in new_num_list:
                multiplied_list.append(i*int(to_multiply))
            print("Given list: ", new_num_list)
            print("New List after multpliying each integer: ", multiplied_list)
        except:
            print("Invalid List Is Given")
    else:
        print("Wrong Input Is Given")


user_input_len_list = input("Enter length of list: ")
user_input_num_list = input("Enter list of number(eg: 25,12,8): ").split(",")
user_input_to_multiply = input("Enter number to multiply the list number: ")
get_multiplied_list(user_input_len_list, user_input_num_list, user_input_to_multiply)