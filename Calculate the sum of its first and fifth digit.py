'''	
Write a program to accept 5 digit integer N and calculate the sum of its first and fifth digit.'''

def get_sum_of_its_first_and_last_digit(num):
    if num.isnumeric() and len(num) == 5:
        list_of_number = list(map(int, num.strip()))
        print(list_of_number[0] + list_of_number[-1])
    else:
        print("Wrong Input Given")

user_input = input("Enter Number of 5 digits: ")
get_sum_of_its_first_and_last_digit(user_input)