import random
import art
from typing import Union

TYPE_OF_MOUSE = (None, "Brown", "Field", "Grey", "White", "Tiny")

def generate_probabilities(cheese_type, enchant=False):
    att_rate = {
        "Cheddar": (0.5, 0.1, 0.15, 0.1, 0.1, 0.05),
        "Marble": (0.6, 0.05, 0.2, 0.05, 0.02, 0.08),
        "Swiss": (0.7, 0.01, 0.05, 0.05, 0.04, 0.15)
    }
    
    if cheese_type == "Swiss" and enchant == True:
        tiny_mouse_prob = 0.4 #att_rate[cheese_type][5] + 0.25
        tiny_mouse_att = 0.45 #att_rate[cheese_type][0] - 0.25
        att_rate[cheese_type] = (
            tiny_mouse_att,
            att_rate[cheese_type][1],
            att_rate[cheese_type][2],
            att_rate[cheese_type][3],
            att_rate[cheese_type][4],
            tiny_mouse_prob
        )
    
    return att_rate[cheese_type]

def generate_mouse(cheese="Cheddar", enchant=False) -> str:
    att_rate = generate_probabilities(cheese, enchant)
    rand = random.random()
    
    if rand < att_rate[0]:
        spawn_mouse = TYPE_OF_MOUSE[0]
    elif att_rate[0] <= rand < sum(att_rate[:2]):
        spawn_mouse = TYPE_OF_MOUSE[1]
    elif sum(att_rate[:2]) <= rand < sum(att_rate[:3]):
        spawn_mouse = TYPE_OF_MOUSE[2]
    elif sum(att_rate[:3]) <= rand < sum(att_rate[:4]):
        spawn_mouse = TYPE_OF_MOUSE[3]
    elif sum(att_rate[:4]) <= rand < sum(att_rate[:5]):
        spawn_mouse = TYPE_OF_MOUSE[4]
    elif sum(att_rate[:5]) <= rand < 1:
        spawn_mouse = TYPE_OF_MOUSE[5]

    return spawn_mouse


def loot_lut(mouse_type: Union[str, None]) -> tuple:
    gold = 0
    points = 0
    spawn_mouse = mouse_type

    if spawn_mouse == "Brown":
        gold += 125
        points += 115
    elif spawn_mouse == 'Field':
        gold += 200
        points += 200
    elif spawn_mouse == 'Grey':
        gold += 125
        points += 90
    elif spawn_mouse == 'White':
        gold += 100
        points += 70
    elif spawn_mouse == 'Tiny':
        gold += 900
        points += 200
    elif mouse_type == None:
        gold += 0
        points += 0

    return (gold, points)

def generate_coat(mouse_type: str) -> str:
    coat_of_arms = ""

    if mouse_type == "Brown":
        coat_of_arms = art.BROWN
    elif mouse_type == "Field":
        coat_of_arms = art.FIELD
    elif mouse_type == "Grey":
        coat_of_arms = art.GREY
    elif mouse_type == "White":
        coat_of_arms = art.WHITE
    elif mouse_type == "Tiny":
        coat_of_arms = art.TINY

    return coat_of_arms


class Mouse:
    def __init__(self, cheese_type="Cheddar", enchant=False):
        self.mouse_type = generate_mouse(cheese_type, enchant)
        self.gold_reward, self.points = loot_lut(self.mouse_type)
        self.coat_of_arms = generate_coat(self.mouse_type)

    def get_name(self) -> str:
        return self.mouse_type

    def get_gold(self) -> int:
        return self.gold_reward
    
    def get_points(self) -> int:
        return self.points
    
    def __str__(self) -> str:
        return "{}".format(self.mouse_type)