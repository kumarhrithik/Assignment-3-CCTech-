'''Write a program to accept number of circles N and radius and coordinates of center (x,y) for each circle. 
Select appropriate data structure and explain why you chose it. Arrange the circles in increasing order of their area and print all the data of each circle.'''

''' I have selected the list and dictionary data structure, in list we can keep the data together and perform the same methods and operation across multiple
and dictionary differs from other data structure that uses two elements namely key and value, we can put value which represent by key'''

from math import pi

user_input_num_of_circle = int(input("Enter number of circle: "))
n_loop = int(user_input_num_of_circle)
num = 1
area = {}
circle_dimension = {}
while n_loop > 0:
    n_loop -= 1
    user_input_circle_dimension = input("Enter Dimensions of circle"+" "+str(num)+" "+"(eg:radius,cordinate_x,cordinate_y): ").split(",")
    circle_dimension["Circle {0}".format(num)] = user_input_circle_dimension
    area["Circle {0}".format(num)] = (pi * int(user_input_circle_dimension[0])**2)
    num += 1
circle_list_ascending_order = sorted(list(area.values()))
print("Circle Data in Ascending Order by AREA as follows: ")
for i in circle_list_ascending_order:
    for key, value in area.items():
        if value == i:
            radius = circle_dimension[key][0]
            x_cordinate = circle_dimension[key][1]
            y_cordinate = circle_dimension[key][2]
            circle_area = i
            print(key+" data as follows: ")
            print("Radius: ", radius)
            print("X-Coordinate: ", x_cordinate)
            print("Y-Coordinate: ", y_cordinate)
            print("Area: ", circle_area)

    