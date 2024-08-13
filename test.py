from shop import buy_cheese
from game import change_cheese
from mouse import Mouse

def cheddar_1():
    gold = 100
    expected = (10, (1, 0, 0))
    assert buy_cheese(gold) == expected, "Test cheddar_1: Failed!"
    print("Test cheddar_1: Passed!")

def marble_2():
    gold = 200
    expected = (100, (0, 2, 0))
    assert buy_cheese(gold) == expected, "Test marble_2: Failed!"
    print("Test marble_2: Passed!")

def gouda_3():
    gold = 50
    expected = (0, (0, 0, 0))
    assert buy_cheese(gold) == expected, "Test gouda_3: Failed!"
    print("Test gouda_3: Passed!")

def negative_4():
    gold = 100
    expected = (0, (0, 0, 0))
    assert buy_cheese(gold) == expected, "Test negative_4: Failed!"
    print("Test negative_4: Passed!")

def insufficient_5():
    gold = 0
    expected = (0, (0, 0, 0))
    assert buy_cheese(gold) == expected, "Test insufficient_5: Failed!"
    print("Test insufficient_5: Passed!")

def maximum_6():
    gold = 214748364700
    expected = (214748364700, (0, 0, 2147483647))
    assert buy_cheese(gold) == expected, "Test maximum_6: Failed!"
    print("Test maximum_6: Passed!")

def armed_cheddar():
    cheese = [("cheddar", 5), ("marble", 3), ("swiss", 2)]
    e_flag = False
    name = "Bob"
    trap = "Cardboard and Hook Trap"
    trap_status, trap_cheese = change_cheese(name, trap, cheese)
    assert trap_status == True and trap_cheese == "Cheddar", "Test armed_cheddar: Failed!"
    print("Test armed_cheddar: Passed!")


def armed_marble():
    cheese = [("Cheddar", 0), ("Marble", 4), ("Swiss", 0)]
    e_flag = False
    name = "Bob"
    trap = "Cardboard and Hook Trap"
    trap_status, trap_cheese = change_cheese(name, trap, cheese)
    assert trap_status == True and trap_cheese == "Marble", "Test armed_marble: Failed!"
    print("Test armed_marble: Passed!")

def no_cheese():
    cheese = [("Cheddar", 0), ("Marble", 0), ("Swiss", 0)]
    e_flag = False
    name = "Bob"
    trap = "Cardboard and Hook Trap"
    trap_status, trap_cheese = change_cheese(name, trap, cheese)
    assert trap_status == False and trap_cheese == None, "Test no_cheese: Failed!"
    print("Test no_cheese: Passed!")


def wrong_name():
    cheese = [("Cheddar", 3), ("Marble", 0), ("Swiss", 0)]
    e_flag = False
    name = "Bob"
    trap = "Cardboard and Hook Trap"
    trap_status, trap_cheese = change_cheese(name, trap, cheese)
    assert trap_status == False and trap_cheese == None, "Test wrong_name: Failed!"
    print("Test wrong_name: Passed!")

def one_cheddar():
    cheese = [("Cheddar", 1), ("Marble", 0), ("Swiss", 0)]
    e_flag = False
    name = "Bob"
    trap = "Cardboard and Hook Trap"
    trap_status, trap_cheese = change_cheese(name, trap, cheese)
    assert trap_status == True and trap_cheese == "Cheddar", "Test one_cheddar: Failed!"
    print("Test one_cheddar: Passed!")


def back():
    cheese = [("Cheddar", 1), ("Marble", 1), ("Swiss", 1)]
    e_flag = False
    name = "Bob"
    trap = "Cardboard and Hook Trap"
    trap_status, trap_cheese = change_cheese(name, trap, cheese)
    
    assert trap_status == False and trap_cheese == None, "Test back: Failed!"   
    print("Test back: Passed!")

def mouse_probability():
    total = 10000
    types = {
        "Brown": 0.1,
        "Field": 0.15,
        "Grey": 0.1,
        "White": 0.1,
        "Tiny": 0.05,
        None: 0.5
    }
    
    count = dict.fromkeys(types, 0)
    
    i = 0
    while i < total:
        mouse_type = Mouse().get_name()
        count[mouse_type] += 1
        
        i += 1
    
    mouse_types_iter = iter(types.items())
    
    while True:
        try:
            mouse_type, prob = next(mouse_types_iter)
            actual_prob = count[mouse_type] / total
            assert abs(actual_prob - prob) <= 0.05, "Failed for {}!".format(mouse_type)
            print("Passed for {}!".format(mouse_type))         
        except StopIteration:
            break


def main():
    #cheddar_1()
    marble_2()
    #gouda_3()
    #negative_4()
    #insufficient_5()
    #maximum_6()
    #armed_cheddar()
    #armed_marble()
    #no_cheese()
    #wrong_name()
    #one_cheddar()
    #back()
    #mouse_probability()


if __name__ == "__main__":
    main()