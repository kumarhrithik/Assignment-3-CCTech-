'''Write a program to accept an integer N and calculate the sum of its digits. Please note N can have maximum 5 digits.'''

def get_sum_of_its_digit(num):
    if num.isnumeric() and len(num)<=5:
        list_of_number = list(map(int, num.strip()))
        print("Suum of Digits: ", sum(list_of_number))
    else:
        print("Wrong Input Given")

user_input = input("Enter Number(Max. 5 digits): ")
get_sum_of_its_digit(user_input)