TYPE_OF_TRAP = ("Cardboard and Hook Trap", "High Strain Steel Trap", "Hot Tub Trap")
TYPE_OF_CHEESE = ("Cheddar", "Marble", "Swiss")

class Trap:
    def __init__(self):
        self.trap_name = ""
        self.trap_cheese = None
        self.arm_status = False
        self.one_time_enchantment = False

    def set_trap_name(self, trap_name):
        if (trap_name == TYPE_OF_TRAP[0]) or (trap_name == TYPE_OF_TRAP[1]) or (trap_name == TYPE_OF_TRAP[2]):
            self.trap_name = trap_name

    def set_trap_cheese(self, cheese):
        if (cheese == TYPE_OF_CHEESE[0]) or (cheese == TYPE_OF_CHEESE[1]) or (cheese == TYPE_OF_CHEESE[2]):
            self.trap_cheese = cheese

    def set_arm_status(self):
        if self.trap_cheese != None and self.trap_name != "":
            self.arm_status = True

    def set_one_time_enchantment(self, enchanted):
        if self.trap_name != TYPE_OF_TRAP[0]:
            self.one_time_enchantment = enchanted

    def get_trap_name(self):
        return self.trap_name

    def get_trap_cheese(self):
        return self.trap_cheese

    def get_arm_status(self):
        return self.arm_status

    def get_one_time_enchantment(self):
        return self.one_time_enchantment

    @staticmethod
    def get_benefit(cheese_type):
        if cheese_type == "Cheddar":
            return "+25 points drop by next Brown mouse"
        elif cheese_type == "Marble":
            return "+25 gold drop by next Brown mouse"
        elif cheese_type == "Swiss":
            return "+0.25 attraction to Tiny mouse"

    def __str__(self):
        if self.one_time_enchantment == True:
            self.trap_name = f"One-time Enchanted {self.trap_name}"

        return self.trap_name