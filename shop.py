CHEESE_MENU = (("Cheddar", 10), ("Marble", 50), ("Swiss", 100))

def buy_cheese(gold: int) -> tuple:
    cheddar_bought = 0
    marble_bought = 0
    swiss_bought = 0
    total_price = 0
    cheese_bought = (0, 0, 0)

    while True:
        print("You have {} gold to spend.".format(gold))
        gold_spent = input("State [cheese quantity] or enter 'back' to exit: ")

        if gold_spent.lower() == "back":
            break

        cheese_type, cheese_str = "", ""

        try:
            cheese_type, cheese_str = gold_spent.lower().split()
            cheese_quantity = int(cheese_str)
        except ValueError:
            if not cheese_str.isnumeric() and (len(cheese_str) != 0):
                print("Invalid quantity.")
                continue
            
            if (cheese_type != "cheddar") or (cheese_type != "marble") or (cheese_type != "swiss"):
                print("We don't sell {}!".format(gold_spent)) 
                continue

            if not cheese_str:
                print("Missing quantity.")
                continue

        if cheese_quantity <= 0:
            print("Must purchase positive amount of cheese.")
            continue

        if cheese_type == "cheddar":
            price = 10
        elif cheese_type == "marble":
            price = 50
        elif cheese_type == "swiss":
            price = 100
        else:
            print("We don't sell {}!".format(cheese_type))
            continue
        
        total_price_attempt = cheese_quantity * price
        if gold < total_price_attempt:
            print("Insufficient gold.")
            continue

        total_price += total_price_attempt
        gold -= total_price_attempt
        if cheese_type == "cheddar":
            cheddar_bought += cheese_quantity
        elif cheese_type == "marble":
            marble_bought += cheese_quantity
        elif cheese_type == "swiss":
            swiss_bought += cheese_quantity

        cheese_bought = (cheddar_bought, marble_bought, swiss_bought)  
        print("Successfully purchase {} {}.".format(cheese_quantity, cheese_type))
        continue

    return (total_price, cheese_bought)

def display_inventory(gold: int, cheese: list, trap: str) -> None:
    print("Gold - {}".format(gold))
    print("{} - {}".format(cheese[0][0], cheese[0][1]))
    print("{} - {}".format(cheese[1][0], cheese[1][1]))
    print("{} - {}".format(cheese[2][0], cheese[2][1]))
    print("Trap - {}".format(trap))

def main():
    gold = 125
    cheese = [["Cheddar", 0], ["Marble", 0], ["Swiss", 0]]
    trap = 'Cardboard and Hook Trap'
    
    print("Welcome to The Cheese Shop!")
    print("{} - {} gold".format(CHEESE_MENU[0][0], CHEESE_MENU[0][1]))
    print("{} - {} gold".format(CHEESE_MENU[1][0], CHEESE_MENU[1][1]))
    print("{} - {} gold".format(CHEESE_MENU[2][0], CHEESE_MENU[2][1]))

    while True:
        print("\nHow can I help ye?")
        choice = int(input("1. Buy cheese\n2. View inventory\n3. Leave shop\n"))

        if choice == 1:
            total_price, cheese_bought = buy_cheese(gold)
            gold = gold - total_price
            cheese[0][1] += cheese_bought[0]
            cheese[1][1] += cheese_bought[1]
            cheese[2][1] += cheese_bought[2]

        elif choice == 2:
            display_inventory(gold, cheese, trap)

        elif choice == 3:
            break

if __name__ == "__main__":
    main()