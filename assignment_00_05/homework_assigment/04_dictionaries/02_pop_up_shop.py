#def main():
    #fruits = {"apple": 3.5, "mango":6, "banana":2.5, "grapes":3, "lichy":4,"watermelon":5}
    #total_cost = 0
    #for fruits_name in fruits:
        #price= fruits[fruits_name]
        #amount_paid = int(input("How many(" + fruits_name +") do you want to buy?: "))
        #total_cost += (price * amount_paid)
        #print("Your total cost is $" + str(total_cost))


# There is no need to edit code beyond this point

#if __name__ == '__main__':
    #main()

    #2nd meythod
def main():
    fruits = {
        'apple': 1.5,
        'durian': 50,
        'jackfruit': 80,
        'kiwi': 1,
        'rambutan': 1.5,
        'mango': 5
    }

    total_cost = 0
    fruit_bought = {}

    for fruit, price in fruits.items():
        amount = int(input(f"How many {fruit}s would you like to buy? "))
        total_cost += amount * price
        fruit_bought[fruit] = amount

    print("\nYou bought:")
    for fruit, amount in fruit_bought.items():
        if amount > 0:
            print(f"- {amount} {fruit}(s)")

    print(f"\nYour total is: ${total_cost:.2f}")

if __name__ == '__main__':
    main()
    
    
    
