'''Accept cost price(CP) and Selling price(SP) of an item. Calculate the ammount of PROFIT/LOSS made by the seller and print the'''

def get_profit_and_loss(cost_price, selling_price):
    if cost_price.isnumeric() and selling_price.isnumeric():
        if int(cost_price) == int(selling_price):
            print("No Gain, No Loss")
        elif int(cost_price) > int(selling_price):
            loss = int(cost_price) - int(selling_price)
            print("Loss: ", loss)
        elif int(cost_price) < int(selling_price):
            profit = int(selling_price) - int(cost_price)
            print("Profit: ", profit)
    else:
        print("Wrong Input Given")

user_input_cp = input("Enter Cost Price: ")
user_input_sp = input("Enter Selling Price: ")
get_profit_and_loss(user_input_cp, user_input_sp)