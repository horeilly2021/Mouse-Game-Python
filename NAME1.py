def is_valid_length(name: str) -> bool:
    length = 1 <= len(name) <= 9
    return length


def is_valid_start(name: str) -> bool:
    start = name[0].isalpha()
    return start


def is_one_word(name: str) -> bool:
    one_word = False
    if(name.find(" ")==-1):
        one_word = True
    return one_word


def is_valid_name(name: str) -> bool:
    if is_valid_length(name) and is_valid_start(name) and is_one_word(name):
        return True
    else:
        return False