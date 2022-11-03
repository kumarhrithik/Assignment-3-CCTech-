'''Write a program to a accept a list of N integers. Find the largest and the smallest number in the list and their respective positions in the list.'''


def get_max_min_from_list(len_list, num_list):
    if int(len_list) == len(num_list):
        try:
            new_num_list = [int(x) for x in num_list]
            max = new_num_list[0]
            min = new_num_list[0]
            min_num_pos = 1
            max_num_pos = 1
            for i in range(len(new_num_list)):
                if int(new_num_list[i]) > int(max):
                    max = new_num_list[i]
                    max_num_pos = i+1
                if int(new_num_list[i]) < int(min):
                    min = new_num_list[i]
                    min_num_pos = i+1
            print("Largest No. on the list: ", max)
            print("Position of largest number on the list: ", max_num_pos)
            print("Smallest No. on the list: ", min)
            print("Position of smallest number on the list: ", min_num_pos)
        except:
            print("Invalid list is given")
    else:
        print("Wrong Input Given")

user_input_len_list = input("Enter length of list: ")
user_input_num_list = input("Enter list of number(eg: 25,12,8): ").split(",")
get_max_min_from_list(user_input_len_list, user_input_num_list)