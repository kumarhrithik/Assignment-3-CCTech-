'''Write a program to accept a 5 digit integer N and then generates a number M by adding 1 to each digit.'''

def adding_1_in_each_digit(num):
    if num.isnumeric() and len(num) == 5:
        list_of_number = list(map(int, num.strip()))
        # print(list_of_number)
        new_list_of_number = []
        for i in list_of_number:
            if i == 9:
                new_list_of_number.append(0)
            else:
                new_list_of_number.append(i+1)
        new_num = ''.join(map(str,new_list_of_number))
        print("New num (added 1 to each digit of given number): ", new_num)
    else:
        print("Wrong Input Given")

user_input = input("Enter Number of 5 digits: ")
adding_1_in_each_digit(user_input)