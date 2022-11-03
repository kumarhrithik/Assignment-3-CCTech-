'''Write a program to accept an integer N and generate an integer M which is formed by reversing the digits of N. Please note N can have maximum 5 digits'''

def reverse_integer(num):
    if num.isnumeric() and len(num)<=5:
        new_num = num[::-1]
        print("Reversed Number is :", int(new_num))
    else:
        print("Wrong Input Given")

user_input = input("Enter a number to reverse it(Max. 5 digits): ")
reverse_integer(user_input)