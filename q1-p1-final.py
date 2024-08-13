def intro():
    print("Larry: I'm Larry. I'll be your hunting instructor.")

def travel_to_camp():
    print("Larry: Let's go to the Meadow to begin your training!")
    skip1 = input("Press Enter to travel to the Meadow...")
    if skip1 == "\x1B":
        return False

    print("Travelling to the Meadow...\nLarry: This is your camp. Here you'll set up your mouse trap.")
    return True

def setup_trap() -> tuple:
    left_trap = "High Strain Steel Trap"
    right_trap = "Hot Tub Trap"
    no_trap = "Cardboard and Hook Trap"

    print("Larry: Let's get your first trap...")
    skip2 = input("Press Enter to view traps that Larry is holding...")
    if skip2 == "\x1B":
        return False, 0
        
    print("Larry is holding...\nLeft: {}\nRight: {}".format(left_trap, right_trap))

    trap = input("Select a trap by typing \"left\" or \"right\": ")
    trap = trap.lower().strip()

    if trap == "left":
        trap = left_trap
        print("Larry: Excellent choice.\nYour \"{}\" is now set!\nLarry: You need cheese to attract a mouse.\nLarry places one cheddar on the trap!".format(left_trap))
        cheddar = 1
        return trap, cheddar
    elif trap == "right":
        trap = right_trap
        print("Larry: Excellent choice.\nYour \"{}\" is now set!\nLarry: You need cheese to attract a mouse.\nLarry places one cheddar on the trap!".format(right_trap))
        cheddar = 1
        return trap, cheddar
    elif trap == "\x1B":
        return False, 0
    else:
        trap = no_trap
        print("Invalid command! No trap selected.\nLarry: Odds are slim with no trap!")
        cheddar = 0
        return trap, cheddar

def sound_horn() -> str:
    print("Sound the horn to call for the mouse...")
    horn_input = input("Sound the horn by typing \"yes\": ")
    horn_input = horn_input.lower().strip()

    return horn_input

def basic_hunt(cheddar: int, horn_input: str) -> bool:
    hunt_status = False

    if horn_input == "\x1b":
        hunt_status = False
        return hunt_status

    if cheddar == 1 and horn_input == "yes":
        print("Caught a Brown mouse!\nCongratulations. Ye have completed the training.")
        hunt_status = True
    elif cheddar == 0 and horn_input != "yes":
        print("Nothing happens.")
        hunt_status =  False
    else:
        print("Nothing happens.\nTo catch a mouse, you need both trap and cheese!")
        hunt_status =  False

    return hunt_status

def end(hunt_status: bool):
    if hunt_status == True:
        print("Good luck~")


def main():
    hunt_status = False

    intro()
    skip1 = travel_to_camp()
    if skip1 == False:
        return None, False
    while True:
        trap, cheddar = setup_trap()
        if trap == False:
            break
        horn_input = sound_horn()
        if horn_input == "\x1b":
            break
        hunt_status = basic_hunt(cheddar, horn_input)
        end(hunt_status)
        repeat = input("\nPress Enter to continue training and \"no\" to stop training: ")
        repeat = repeat.lower().strip()
        if repeat == "\x1B":
            break
        elif repeat == "no":
            break

    return trap, hunt_status


if __name__ == '__main__':
    main()