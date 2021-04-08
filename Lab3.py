NUM_RUNS = 5    #global
COUP_1= 0.08
COUP_2= 0.1
COUP_3= 0.12
COUP_4= 0.14

def main():
    for index in range(0,NUM_RUNS):
        print(index+1);
        input_data()


def input_data():    # first function for working with input data
    gr = input("Please enter the cost of you groceries:  ")
    while True:                           #check numbers
        try:
            cost = int(input("Enter cost >=0: "))
        except ValueError:
            print("Please, enter numbers")
            continue

        else:
            break
    if cost <= 0:                     # check negative numbers
        cost = eval(input("Enter cost >=0: "))
    count_discount(cost)



def count_discount(cost): #second function for counting of discount + output
    if cost < 10:
        coupon = 0
    elif cost >=10 and cost <60:
        coupon = COUP_1
    elif cost >= 60 and cost<150:
        coupon = COUP_2
    elif cost >=150 and cost<210:
        coupon = COUP_3
    elif cost >= 210:
        coupon = COUP_4

    discount = cost * coupon
    discount= format(discount,'10.2f')
    coupon = round(coupon * 100)

    print("You win a discount coupon of: {discount} $   ( {coupon}% of\
 your purchase.)".format(coupon=coupon, discount=discount))


main() # main entry
