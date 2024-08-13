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
    if is_valid_length(name) and is_valid_start(name) and is_one_word(name) and not is_profanity(name):
        return True
    else:
        return False


def is_profanity(word: str, database='/home/files/list.txt', records='/home/files/history.txt') -> bool:
    result = False

    try:
        with open(database, 'r') as f:
            lines = f.readlines()

            i = 0
            while i < len(lines) and not result:
                if lines[i].strip() == word:
                    result = True

                    with open(records, 'a') as g:
                        g.write(word + "\n")

                else:
                    i += 1
                    continue

    except FileNotFoundError:
        print("Check directory of database!")

    return result


def count_occurrence(word: str, file_records="/home/files/history.txt", start_flag=True) -> int:
    count = 0

    if not isinstance(word, str):
        print("First argument must be a string object!")

    elif len(word) <= 0:
        print("Must have at least one character in the string!")

    else:
        try:
            with open(file_records, 'r') as f:
                while True:
                    line = f.readline()
                    if line == "":
                        break
                    elif start_flag == True:
                        if line.lower().startswith(word[0].lower()):
                            count += 1
                    else:
                        count += line.lower().count(word.lower())

        except FileNotFoundError:
            print("File records not found!")
            
    return count


def generate_name(word: str, src="/home/files/animals.txt", past="/home/files/names.txt") -> str:
    if not isinstance(word, str):
        print("First argument must be a string object!")
        return "Bob"

    if len(word) == 0:
        print("Must have at least one character in the string!")
        return "Bob"
    
    try:
        with open(src) as f:
            lines = []
            while True:
                line = f.readline()
                if line == "":
                    break
                if line.strip()[0].lower() == word[0].lower():
                    lines.append(line.strip())

        if len(lines) == 0:
            print("No suitable replacement names found in the source file!")
            return "Bob"

        past_names = []
        try:
            with open(past) as g:
                while True:
                    line = g.readline()
                    if line == "":
                        break
                    past_names.append(line.strip())

        except FileNotFoundError:
            print("Source file is not found!")
            return "Bob"

        i = 0
        least_common_name = lines[i]
        least_common_count = float('inf')
        while i < len(lines):
            name = lines[i]
            found = False
            j = 0
            while j < len(past_names):
                if past_names[j] == name:
                    found = True
                    break
                j += 1
                
            if not found:
                count = count_occurrence(name, past, start_flag=True)
                if count < least_common_count:
                    least_common_count = count
                    least_common_name = name
                    
            i += 1

        new_name = least_common_name
        
        with open(past, "a") as h:
            h.write(new_name + "\n")

        return new_name

    except FileNotFoundError:
        print("Source file is not found!")
        return "Bob"


def main():
    while True:
        name = input("Check name: ")
        if name == "s":
            break
        
        if is_valid_name(name):
            print("{} is a valid name!".format(name))
        else:
            new_name = generate_name(name)
            print("Your new name is: {}".format(new_name))


if __name__ == "__main__":
    main()