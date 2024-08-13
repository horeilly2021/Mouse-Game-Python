import shop
from hunter import Hunter

class CheeseShop:
    def __init__(self):
        self.cheeses = {"Cheddar": 10, "Marble": 50, "Swiss": 100}
        self.menu = {1: "Buy cheese", 2: "View inventory", 3: "Leave shop"}

    def get_cheeses(self):
        cheeses_sold = f'''Cheddar - {self.cheeses["Cheddar"]} gold
Marble - {self.cheeses["Marble"]} gold
Swiss - {self.cheeses["Swiss"]} gold'''

        return cheeses_sold

    def get_menu(self):
        menu_str = f'''1. {self.menu[1]}
2. {self.menu[2]}
3. {self.menu[3]}'''

        return menu_str

    def greet(self):
        greeting = f'''Welcome to The Cheese Shop!
Cheddar - {self.cheeses["Cheddar"]} gold
Marble - {self.cheeses["Marble"]} gold
Swiss - {self.cheeses["Swiss"]} gold'''

        return greeting
    
    def buy_cheese(self, gold: int):
        total_price, cheese_bought = shop.buy_cheese(gold)
        gold = gold - total_price

        return gold, cheese_bought

    def move_to(self, player: Hunter):
        while True:
            print("How can I help ye?")
            print(self.get_menu())

            try:
                shop_attempt = int(input())
                if not isinstance(shop_attempt, int):
                    raise ValueError
            except ValueError: 
                print("I did not understand.\n")
                continue

            if int(shop_attempt) < 1 or int(shop_attempt) > 3:
                raise ValueError

            if shop_attempt == 1:
                self.gold, self.cheeses_bought = self.buy_cheese(player.gold)
                player.gold = self.gold
                player.update_cheese(self.cheeses_bought)
                print("")
            elif shop_attempt == 2:
                print(player.display_inventory())
                print("")
            elif shop_attempt == 3:
                break