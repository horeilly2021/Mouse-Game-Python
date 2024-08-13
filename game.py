import random
import NAME1
import train
import shop
import title

from train import main as main_train
from typing import Union

def get_game_menu():
    game_menu = '''1. Exit game
2. Join the Hunt
3. The Cheese Shop
4. Change Cheese'''
    return game_menu

def change_cheese(name: str, trap: str, cheese: list, e_flag: bool = False) -> tuple:
    trap_status = False
    trap_cheese = None

    while True:
        print("Hunter {}, you currently have:".format(name))
        print("{} - {}".format(cheese[0][0], cheese[0][1]))
        print("{} - {}".format(cheese[1][0], cheese[1][1]))
        print("{} - {}\n".format(cheese[2][0], cheese[2][1]))

        choosing_trap_cheese = input("Type cheese name to arm trap: ")
        choosing_trap_cheese = choosing_trap_cheese.lower().strip()
        if choosing_trap_cheese == "cheddar":
            if cheese[0][1] > 0:
                trap_cheese = "Cheddar"
                trap_status = True
            else:
                print("Out of cheese!\n")
                continue
        elif choosing_trap_cheese == "marble":
            if cheese[1][1] > 0:
                trap_cheese = "Marble"
                trap_status = True
            else:
                print("Out of cheese!\n")
                continue
        elif choosing_trap_cheese == "swiss":
            if cheese[2][1] > 0:
                trap_cheese = "Swiss"
                trap_status = True
            else:
                print("Out of cheese!\n")
                continue
        elif choosing_trap_cheese == "back":
            break
        else:
            print("No such cheese!\n")
            continue

        if trap_status == True:
            if e_flag == True and trap_cheese == "Cheddar":
                print("Your One-time Enchanted {} has a one-time enchantment granting +25 points drop by next Brown mouse.".format(trap))
            if e_flag == True and trap_cheese == "Marble":
                print("Your One-time Enchanted {} has a one-time enchantment granting +25 gold drop by next Brown mouse.".format(trap))
            elif e_flag == True and trap_cheese == "Swiss":
                print("Your One-time Enchanted {} has a one-time enchantment granting +0.25 attraction to Tiny mouse.".format(trap))
                
            arming_trap = input("Do you want to arm your trap with {}? ".format(trap_cheese))
            arming_trap = arming_trap.lower().strip()
            if arming_trap == "yes":
                if e_flag == True:
                    print("One-time Enchanted {} is now armed with {}!".format(trap, trap_cheese))
                else:
                    print("{} is now armed with {}!".format(trap, trap_cheese))
                break
            elif arming_trap == "back":
                trap_status = False
                trap_cheese = None
                break
            elif arming_trap == "no":
                print("")
                trap_status = False
                trap_cheese = None
                continue

    return trap_status, trap_cheese

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

def hunt(gold: int, cheese: list, trap_cheese: Union[str, None], points: int) -> tuple:
    consecutive_fails = 0

    while True:
        print("Sound the horn to call for the mouse...")
        horn_choice = input("Sound the horn by typing 'yes' or exit by entering 'stop': ")
        horn_choice = horn_choice.strip()

        if horn_choice == "stop":
            break
        elif horn_choice != "yes":
            print("Do nothing.")
            consecutive_fails += 1
            print("My gold: {}, My points: {}\n".format(gold, points))
        else:
            if trap_cheese == None:
                print("Nothing happens. You are out of cheese!")
                consecutive_fails += 1
            elif trap_cheese.lower() == "cheddar":
                if cheese[0][1] > 0:
                    if random.random() <= 0.5:
                        print("Caught a Brown mouse!")
                        gold += 125
                        points += 115
                        consume_cheese(trap_cheese, cheese)
                        consecutive_fails = 0
                    else:
                        print("Nothing happens.")
                        consume_cheese(trap_cheese, cheese)
                        consecutive_fails += 1
                else:
                    print("Nothing happens. You are out of cheese!")
                    consecutive_fails += 1
            elif trap_cheese.lower() == "marble":
                if cheese[1][1] > 0:
                    if random.random() <= 0.5:
                        print("Caught a Brown mouse!")
                        gold += 125
                        points += 115
                        consume_cheese(trap_cheese, cheese)
                        consecutive_fails = 0
                    else:
                        print("Nothing happens.")
                        consume_cheese(trap_cheese, cheese)
                        consecutive_fails += 1
                else:
                    print("Nothing happens. You are out of cheese!")
                    consecutive_fails += 1
            elif trap_cheese.lower() == "swiss":
                if cheese[2][1] > 0:
                    if random.random() <= 0.5:
                        print("Caught a Brown mouse!")
                        gold += 125
                        points += 115
                        consume_cheese(trap_cheese, cheese)
                        consecutive_fails = 0
                    else:
                        print("Nothing happens.")
                        consume_cheese(trap_cheese, cheese)
                        consecutive_fails += 1
                else:
                    print("Nothing happens. You are out of cheese!")
                    consecutive_fails += 1

            print("My gold: {}, My points: {}\n".format(gold, points))

        if consecutive_fails >= 5:
            continue_hunting = input("Do you want to continue to hunt? ")
            continue_hunting = continue_hunting.strip()
            if continue_hunting == "no":
                break
            else:
                consecutive_fails = 0

    return gold, points

def main():
    cheese = [["Cheddar", 0], ["Marble", 0], ["Swiss", 0]]
    trap_cheese = None
    gold = 125
    points = 0

    title.game_title()

    name = input("What's ye name, Hunter?\n") 
    if NAME1.is_valid_name(name) == True:
        name = name
    else:
        name = "Bob"

    print("Welcome to the Kingdom, Hunter {}!".format(name))
    print("Before we begin, let's train you up!")
    train_choice = input("Press \"Enter\" to start training or \"skip\" to Start Game: ")
    if train_choice != "skip":
        print("")
        trap, hunt_status = main_train()
        if trap == None or trap == False:
            trap = "Cardboard and Hook Trap"
    else:
        trap = "Cardboard and Hook Trap"

    while True:
        print("\nWhat do ye want to do now, Hunter {}?".format(name))
        game_menu = get_game_menu()
        print(game_menu)
        choice = int(input())

        if choice == 1:
            break
        elif choice == 2:
            gold, points = hunt(gold, cheese, trap_cheese, points)
        elif choice == 3:
            print("Welcome to The Cheese Shop!")
            print("Cheddar - 10 gold")
            print("Marble - 50 gold")
            print("Swiss - 100 gold")
            while True:
                print("\nHow can I help ye?")
                print("1. Buy cheese")
                print("2. View inventory")
                print("3. Leave shop")
                shop_choice = int(input())
                
                if shop_choice == 1:
                    gold_spent, cheese_bought = shop.buy_cheese(gold)
                    gold -= gold_spent
                    cheese[0][1] += cheese_bought[0]
                    cheese[1][1] += cheese_bought[1]
                    cheese[2][1] += cheese_bought[2]
                elif shop_choice == 2:
                    shop.display_inventory(gold, cheese, trap)
                elif shop_choice == 3:
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif choice == 4:
            trap_status, trap_cheese = change_cheese(name, trap, cheese, e_flag= False)
        else:
            print("Invalid choice. Please try again")
            continue
    

if __name__ == '__main__':
    main()