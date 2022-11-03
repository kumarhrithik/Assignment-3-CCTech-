'''Write a program to accept a list L1 of N integers. Accept integer D. Generate list L2 such that it contains only those integers from list L1 which are divisible by D. 
Calculate the size of list L2. Print the list L1, N, D, list L2 and its size.'''

def get_list_which_divisible_by(len_list, num_list, divisible_by):
    if int(len_list) == len(num_list) and divisible_by.isnumeric():
        try:
            new_num_list = [int(x) for x in num_list]
            divisible_list = []
            for i in new_num_list:
                if i % int(divisible_by) == 0:
                    divisible_list.append(i)
            print("Given list: ", new_num_list)
            print("Length of given list: ", len_list)
            print("To find list which is Divisible by: ", divisible_by)
            print("New list after divisible: ", divisible_list)
            print("Length of New list: ", len(divisible_list))
        except:
            print("Invalid List Is Given")
    else:
        print("Wrong Input Is Given")

user_input_len_list = input("Enter length of list: ")
user_input_num_list = input("Enter list of number(eg: 25,12,8): ").split(",")
user_input_divisible_by = input("Enter number to find list which is Divisible by: ")
get_list_which_divisible_by(user_input_len_list,user_input_num_list, user_input_divisible_by)