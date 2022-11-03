'''Write a program to accept an integer N and generate an integer M which is formed by reversing the digits of N. Please note N can have maximum 5 digits.
   Print the numbers N and M. Compare N with M and print the result'''

def compare_given_and_reverse_integer(num):
    if num.isnumeric() and len(num)<=5:
        new_num = num[::-1]
        if int(new_num) == int(num):
            print("Given Number(N) is ", int(num))
            print("Revesed Number(M) is ", int(new_num))
            print("Number(N) And Reversed Number(M) is EQUAL")
        elif int(new_num) > int(num):
            print("Given Number(N) is ", int(num))
            print("Revesed Number(M) is ", int(new_num))
            print("Reversed Number(M) is GREATER THAN Given Number(N)")
        elif int(new_num) < int(num):
            print("Given Number(N) is ", int(num))
            print("Revesed Number(M) is ", int(new_num))
            print("Reversed Number(M) is SMALLER THAN Given Number(N)")

    else:
        print("Wrong Input Given")

user_input = input("Enter a number(N) to Reverse_Number(M) it(Max. 5 digits): ")
compare_given_and_reverse_integer(user_input)