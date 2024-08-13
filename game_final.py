import title
import name
import game
import shop
import art

from mouse import Mouse
from train import main as main_train

def personalization():
    hunter_name = input("What's ye name, Hunter? ")
    if name.is_valid_name(hunter_name) == True:
        hunter_name = hunter_name
    else:
        print("That's not nice!")
        print("I'll give ye 3 attempts to get it right or I'll name ye!")
        print("Let's try again...")
        new_name = input("What's ye name, Hunter? ")
        if  name.is_valid_name(new_name) == True:
            hunter_name = new_name
        else:
            print("Nice try. Strike 1!")
            new_name = input("What's ye name, Hunter? ")           
            if name.is_valid_name(new_name) == True:
                hunter_name = new_name
            else:                
                print("Nice try. Strike 2!")
                new_name = input("What's ye name, Hunter? ")
                if name.is_valid_name(new_name) == True:
                    hunter_name = new_name
                else:
                    print("Nice try. Strike 3!")
                    print("I told ye to be nice!!!")
                    hunter_name = name.generate_name(hunter_name)

    return hunter_name

def get_choice():
    while True:
        num_choice = input("Enter a number between 1 and 4: ")
        if not num_choice.isnumeric():
            print("Invalid input.")
            continue
        elif int(num_choice) < 1 or int(num_choice) > 4:
            print("Must be between 1 and 4.")
            continue
        else:
            return int(num_choice)
        
def get_shop_choice():
    while True:
        print("\nHow can I help ye?")
        print("1. Buy cheese")
        print("2. View inventory")
        print("3. Leave shop")
        shop_attempt = input()
        if not shop_attempt.isdigit():
            print("I did not understand.")
            continue
        elif int(shop_attempt) < 1 or int(shop_attempt) > 3:
            print("I did not understand.")
            continue
        else:
            return int(shop_attempt)
        
def enchanted_inventory(gold: int, cheese: list, trap: str) -> None:
    print("Gold - {}".format(gold))
    print("{} - {}".format(cheese[0][0], cheese[0][1]))
    print("{} - {}".format(cheese[1][0], cheese[1][1]))
    print("{} - {}".format(cheese[2][0], cheese[2][1]))
    print("Trap - One-time Enchanted {}".format(trap))

def get_benefit(cheese: list) -> str:
    if cheese == "Cheddar":
        benefit = "+25 points drop by next Brown mouse."
    if cheese == "Marble":
        benefit = "+25 gold drop by next Brown mouse."
    if cheese == "Swiss":
        benefit = "+0.25 attraction to Tiny mouse."

    return benefit

def consume_cheese(to_eat: str, cheese: str):
    if to_eat == "Cheddar":
        hunting_cheese = cheese[0][1]
        if hunting_cheese <= 0:
            cheese[0][1] -= 0
        else:
            cheese[0][1] -= 1
    elif to_eat == "Marble":
        hunting_cheese = cheese[1][1]
        if hunting_cheese <= 0:
            cheese[1][1] -= 0
        else:
            cheese[1][1] -= 1
    elif to_eat == "Swiss":
        hunting_cheese = cheese[2][1]
        if hunting_cheese <= 0:
            cheese[2][1] -= 0
        else:
            cheese[2][1] -= 1

def has_cheese(to_check: str, my_cheese: list):
    i = 0
    while i < len(my_cheese):
        if my_cheese[i][0] == to_check:
            return my_cheese[i][1]
        i += 1
    return 0

def hunt(gold: int, cheese: list, trap_cheese: str, enchant: bool, points: int) -> tuple:
    consecutive_fails = 0

    while True:
        print("Sound the horn to call for the mouse...")
        horn_choice = input("Sound the horn by typing 'yes' or 'stop' to exit: ")
        horn_choice = horn_choice.strip()

        if horn_choice == "stop":
            enchant = False
            break
        elif horn_choice != "yes":
            print("Do nothing.")
            consecutive_fails += 1
            enchant = False
        else:
            if has_cheese(trap_cheese, cheese) <= 0:
                print("Nothing happens. You are out of cheese!")
                consecutive_fails += 1
                enchant = False

            else:
                hunting_mouse = Mouse(cheese_type=trap_cheese, enchant=enchant)
                if hunting_mouse.mouse_type == None:
                    print("Nothing happens.")
                    consume_cheese(trap_cheese, cheese)
                    consecutive_fails += 1
                    enchant = False   

                else:
                    print("Caught a {} mouse!".format(hunting_mouse))
                    print(hunting_mouse.coat_of_arms)
                    if enchant == True and trap_cheese == "Cheddar" and hunting_mouse.mouse_type == "Brown":
                        points += 25
                    elif enchant == True and trap_cheese == "Marble" and hunting_mouse.mouse_type == "Brown":
                        gold += 25 
                    gold += hunting_mouse.gold_reward
                    points += hunting_mouse.points
                    consume_cheese(trap_cheese, cheese)
                    consecutive_fails = 0
                    enchant = False

        print("My gold: {}, My points: {}\n".format(gold, points))

        if consecutive_fails >= 5:
            continue_hunting = input("Do you want to continue to hunt? ")
            continue_hunting = continue_hunting.strip()
            if continue_hunting == "no":
                break
            else:
                consecutive_fails = 0

    return gold, cheese, points

def main():
    cheese = [["Cheddar", 0], ["Marble", 0], ["Swiss", 0]]
    trap_cheese = None
    gold = 125
    points = 0
    enchant = False
    hunt_status = False

    print('''Launching game...
.
.
.''')

    title.game_final_title()

    hunter_name = personalization()
    print("Welcome to the Kingdom, Hunter {}!".format(hunter_name))

    print("Before we begin, let's train you up!")
    train_choice = input("Press \"Enter\" to start training or \"skip\" to Start Game: ")

    trap = "Cardboard and Hook Trap"

    if train_choice != "skip":
        print("")
        trap, hunt_status = main_train()
        if hunt_status == True:
            enchant = True
    else:
        trap = "Cardboard and Hook Trap"

    while True:
        print("\nWhat do ye want to do now, Hunter {}?".format(hunter_name))
        game_menu = game.get_game_menu()
        print(game_menu)

        choice = get_choice()

        if choice == 1:
            break
        elif choice == 2:
            gold, cheese, points = hunt(gold, cheese, trap_cheese, enchant, points)
            enchant = False
        elif choice == 3:
            print("\nWelcome to The Cheese Shop!")
            print("Cheddar - 10 gold")
            print("Marble - 50 gold")
            print("Swiss - 100 gold")
            while True:
                shop_choice = get_shop_choice()
                
                if shop_choice == 1:
                    gold_spent, cheese_bought = shop.buy_cheese(gold)
                    gold -= gold_spent
                    cheese[0][1] += cheese_bought[0]
                    cheese[1][1] += cheese_bought[1]
                    cheese[2][1] += cheese_bought[2]
                elif shop_choice == 2:
                    if enchant == True:
                        enchanted_inventory(gold, cheese, trap)
                    else:
                        shop.display_inventory(gold, cheese, trap)
                elif shop_choice == 3:
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif choice == 4:
            print("")
            trap_status, trap_cheese = game.change_cheese(hunter_name, trap, cheese, enchant)

if __name__ == '__main__':
    main()