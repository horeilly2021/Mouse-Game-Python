import game_final
from hunter import Hunter
from cshop import CheeseShop

player = Hunter()

class Interface:
    def __init__(self):
        self.menu = {1: "Exit game", 2: "Join the Hunt", 3: "The Cheese Shop", 4: "Change Cheese"}
        self.player = player

    def set_player(self, player: Hunter):
        if isinstance(player, Hunter):
            self.player = player
   
    def get_menu(self):
        menu_str = f'''1. {self.menu[1]}
2. {self.menu[2]}
3. {self.menu[3]}
4. {self.menu[4]}'''

        return menu_str
    
    def change_cheese(self):
        while True:
            print("Hunter {}, you currently have:".format(self.player.name))
            print(self.player.get_cheese())

            choosing_trap_cheese = input("\nType cheese name to arm trap or 'back' to exit: ")
            choosing_trap_cheese = choosing_trap_cheese.lower().strip()

            if choosing_trap_cheese == "back":
                self.player.trap.arm_status = False
                self.player.trap.trap_cheese = None
                break
            elif choosing_trap_cheese != "cheddar" and choosing_trap_cheese != "marble" and choosing_trap_cheese != "swiss":
                print("No such cheese!\n")
                continue
            elif self.player.have_cheese(choosing_trap_cheese.capitalize()) <= 0:
                print("Out of cheese!\n")
                continue
            else:
                self.player.trap.trap_cheese = choosing_trap_cheese.capitalize()
                self.player.arm_trap(self.player.trap.trap_cheese)
            
            
            
            if self.player.trap.arm_status == True:
                if self.player.trap.one_time_enchantment == True and self.player.trap.trap_cheese == "Cheddar":
                    print("Your One-time Enchanted {} has a one-time enchantment granting +25 points drop by next Brown mouse.".format(self.player.trap.trap_name))
                elif self.player.trap.one_time_enchantment == True and self.player.trap.trap_cheese == "Marble":
                    print("Your One-time Enchanted {} has a one-time enchantment granting +25 gold drop by next Brown mouse.".format(self.player.trap.trap_name))
                elif self.player.trap.one_time_enchantment == True and self.player.trap.trap_cheese == "Swiss":
                    print("Your One-time Enchanted {} has a one-time enchantment granting +0.25 attraction to Tiny mouse.".format(self.player.trap.trap_name))

            arming_trap = input("Do you want to arm your trap with {}? ".format(self.player.trap.trap_cheese))
            arming_trap = arming_trap.lower().strip()

            if arming_trap == "yes":
                if self.player.trap.one_time_enchantment == True:
                    print("You are now armed with One-time Enchanted {}!".format(self.player.trap.trap_cheese))
                else:
                    print("You are now armed with {}!".format(self.player.trap.trap_cheese))
                break
            elif arming_trap == "back":
                self.player.trap.arm_status = False
                self.player.trap.trap_cheese = None
                break
            elif arming_trap == "no":
                print("")
                self.player.trap.arm_status = False
                self.player.trap.trap_cheese = None
                continue

        return self.player.arm_trap(self.player.trap.trap_cheese)
    
    def cheese_shop(self):
        cheese_shop = CheeseShop()
        cheese_shop.move_to(self.player)

    def hunt(self):
        gold, cheese, points = game_final.hunt(self.player.gold, self.player.cheese, self.player.trap.trap_cheese, self.player.trap.one_time_enchantment, self.player.points)
        self.player.gold = gold
        self.player.cheese = cheese
        self.player.points = points
        self.player.trap.one_time_enchantment = False

    def move_to(self, choice: int):
        try:
            int_choice = int(choice)
            if not isinstance(int_choice, int):
                print("Invalid input. Try again!")
                return True
            elif int_choice < 1 or int_choice > 4:
                print("Must be within 1 and 4.")
                return True
            elif int_choice == 1:
                return False
            elif int_choice == 2:
                self.hunt()
            elif int_choice == 3:
                print(CheeseShop().greet())
                print("")
                self.cheese_shop()
            elif int_choice == 4:
                self.arm_trap = self.change_cheese()
        
        except:
            print("Invalid input. Try again!")
        
        return True