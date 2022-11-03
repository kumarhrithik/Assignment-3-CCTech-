'''Write a program to accept a list of N integers. Accept integer K. 
   Find the Kth smallest number in the list and its position'''


def get_kth_smallest_number(len_list, num_list, position):
    if int(len_list) == len(num_list) and int(position) <= int(len_list):
        try:
            new_num_list = [int(x) for x in num_list]
            sorted_num_list = sorted(new_num_list)
            smallest_num_at_kth_pos = sorted_num_list[int(position)-1]
            position_of_Kth_smallest_integer = 0
            for i in range(len(new_num_list)):
                if new_num_list[i] == int(smallest_num_at_kth_pos):
                    position_of_Kth_smallest_integer = i+1
            print("Kth smallest integer: ", smallest_num_at_kth_pos)
            print("Position of Kth smallest integer: ", position_of_Kth_smallest_integer)
        except:
            print("Invalid List is Given")
    else:
        print("Wrong Input Is Given")
        
user_input_len_list = input("Enter length of list: ")
user_input_num_list = input("Enter list of number(eg: 25,12,8): ").split(",")
user_input_position = input("Enter Kth number: ")
get_kth_smallest_number(user_input_len_list, user_input_num_list, user_input_position)