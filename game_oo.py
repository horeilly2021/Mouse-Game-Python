import title
import game_final

from interface import Interface
from hunter import Hunter

from train import main as main_train

main_menu = Interface()
player = Hunter()

def main():
    print('''Launching game...
.
.
.''')

    title.game_final_title()

    hunter_name = game_final.personalization()
    print("Welcome to the Kingdom, Hunter {}!".format(hunter_name))

    print("Before we begin, let's train you up!")
    train_choice = input("Press \"Enter\" to start training or \"skip\" to Start Game: ")

    player.trap.trap_name = "Cardboard and Hook Trap"

    if train_choice != "skip":
        print("")
        trap_name, hunt_status = main_train()
        if hunt_status == True:
            player.trap.one_time_enchantment = True
            player.trap.trap_name = trap_name
        else:
            player.trap.one_time_enchantment = False
            player.trap.trap_name = trap_name
    else:
        player.trap.trap_name = "Cardboard and Hook Trap"

    while True:
        print("\nWhat do ye want to do now, Hunter {}?".format(hunter_name))
        game_menu = main_menu.get_menu()
        print(game_menu)

        choice = input()

        if not main_menu.move_to(choice):
            break

if __name__ == '__main__':
    main()