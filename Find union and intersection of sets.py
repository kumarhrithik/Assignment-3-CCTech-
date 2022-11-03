'''Write a program to accept cardinality of set A as N, and cardinality of set B as M. Then accept elements of set A and set B. 
Generate set C which is union of set A and set B, set D which is intersection set of set A and Set B. 
Print set A, B, C, D, Cardinality of set C, Cardinality of set D'''


def get_set_union_and_intersection(len_set_a, len_set_b, set_a, set_b):
    if int(len_set_a) == len(set_a) and int(len_set_b) == len(set_b):
        union_set_c = set(set_a) | set(set_b)
        intersection_set_d = set(set_a) & set(set_b)
        print("Set A: ", set(set_a))
        print("Set B: ", set(set_b))
        print("Union of Set A and Set B :", union_set_c)
        print("Intersection of Set A and Set B :", intersection_set_d)
        print("Cardinality of Set C: ", len(union_set_c))
        print("Cardinality of Set D: ", len(intersection_set_d))

    else:
        print("Wrong Input Given")

user_input_len_of_set_a = input("Enter cardinality of Set A: ")
user_input_len_of_set_b = input("Enter cardinality of Set B: ")
user_input_set_a = input("Enter a Set A(eg: 25,15,2): ").split(",")
user_input_set_b = input("Enter a Set b(eg: 25,15,2): ").split(",")
get_set_union_and_intersection(user_input_len_of_set_a, user_input_len_of_set_b, user_input_set_a, user_input_set_b)