import name
from trap import Trap
from typing import Union

TYPE_OF_CHEESE = ("Cheddar", "Marble", "Swiss")

class Hunter:
    def __init__(self):
        self.name = "Bob"
        self.cheese = [["Cheddar", 0], ["Marble", 0], ["Swiss", 0]]
        self.trap = Trap()
        self.gold = 125
        self.points = 0

    def set_name(self, player_name):
        if name.is_valid_name(player_name):
            self.name = player_name

    def set_cheese(self, try_cheese):
        if isinstance(try_cheese, tuple):
            self.cheese[0][1] = try_cheese[0]
            self.cheese[1][1] = try_cheese[1]
            self.cheese[2][1] = try_cheese[2]

    def set_gold(self, try_gold):
        if isinstance(try_gold, int):
            self.gold = try_gold

    def set_points(self, try_points):
        if isinstance(try_points, int):
            self.points = try_points

    def get_name(self):
        return self.name

    def get_cheese(self):
        self.cheese_quant =  f'''Cheddar - {self.cheese[0][1]}
Marble - {self.cheese[1][1]}
Swiss - {self.cheese[2][1]}'''

        return self.cheese_quant

    def get_gold(self):
        return self.gold

    def get_points(self):
        return self.points

    def update_cheese(self, cheese_tuple):
        if isinstance(cheese_tuple, tuple):
            self.cheese[0][1] += cheese_tuple[0]
            self.cheese[1][1] += cheese_tuple[1]
            self.cheese[2][1] += cheese_tuple[2]

    def consume_cheese(self, cheese_type):
        if isinstance(cheese_type, str):
            if cheese_type == "Cheddar" and self.cheese[0][1] > 0:
                self.cheese[0][1] -= 1
            elif cheese_type == "Marble" and self.cheese[1][1] > 0:
                self.cheese[1][1] -= 1
            elif cheese_type == "Swiss" and self.cheese[2][1] > 0:
                self.cheese[2][1] -= 1
        

    def have_cheese(self, cheese_type="Cheddar"):
        if isinstance(cheese_type, str):
            if cheese_type == "Cheddar":
                return self.cheese[0][1]
            elif cheese_type == "Marble":
                return self.cheese[1][1]
            elif cheese_type == "Swiss":
                return self.cheese[2][1]
            else:
                return 0
        else:    
            return 0

    def display_inventory(self):
        inventory = f'''Gold - {self.gold}
Cheddar - {self.cheese[0][1]}
Marble - {self.cheese[1][1]}
Swiss - {self.cheese[2][1]}
Trap - {self.trap}'''

        return inventory

    def arm_trap(self, cheese_type: Union[str, None]):
        if isinstance(cheese_type, str) and (cheese_type == "Cheddar" or cheese_type == "Marble" or cheese_type == "Swiss"):
            if self.have_cheese(cheese_type) > 0:
                self.trap.trap_cheese = cheese_type
                self.trap.arm_status = True
            else:
                self.trap.trap_cheese = None
                self.trap.arm_status = False
        else:
            self.trap.trap_cheese = None
            self.trap.arm_status = False

        return self.trap.trap_cheese

    def update_gold(self, hunt_gold):
        if isinstance(hunt_gold, int):
            self.gold += hunt_gold

    def update_points(self, hunt_points):
        if isinstance(hunt_points, int):
            self.points += hunt_points

    def __str__(self):
        inventory = f'''Hunter {self.name}
Gold - {self.gold}
Cheddar - {self.cheese[0][1]}
Marble - {self.cheese[1][1]}
Swiss - {self.cheese[2][1]}
Trap - {self.trap}'''
        
        return inventory