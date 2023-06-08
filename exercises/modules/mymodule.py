import string
from random import randint
all_characteres = string.ascii_letters + string.digits
len_all_characters = len(all_characteres)


def generate_full_name(firstname, lastname):
    return firstname + ' ' + lastname

#Exercises: Level 1
#1. Write a function which generates a six digit/character random_user_id.
def generate_user_id(number_of_characters):
    user_id = ""
    for _ in range (1, number_of_characters):
        user_id  += all_characteres[randint(0, len_all_characters-1)]
    return user_id.lower()

#2. Modify the previous task. Declare a function named user_id_gen_by_user. 
# It doesn’t take any parameters but it takes two inputs using input(). 
# One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
def user_id_gen_by_user():
    number_of_characters = int(input('number of characters: '))
    number_of_ids = int(input('number of IDs: '))
    for i in range(1, number_of_ids+1):
        user_id = generate_user_id(number_of_characters)
        print(i,"user_id:",user_id)

#3. Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
def generate_rgb_color():
    return f"rgb({randint(0, 255)},{randint(0, 255)},{randint(0, 255)})"

#Exercises: Level 2
#2.1 Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array 
# (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 
# 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).

def generate_hexadecimal_color():
    hexa = ""
    for _ in range(0,6):
        hexa += string.hexdigits[randint(0, len(string.hexdigits)-1)]
    return f"#{hexa.upper()}"

def list_of_hexa_colors(size):
    colors = []
    for i in range(0, size):
        colors.append(generate_hexadecimal_color())
    return colors

#2.2 Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
def list_of_rgb_colors(size):
    colors = []
    for i in range(0, size):
        colors.append(generate_rgb_color())
    return colors

def generate_colors(color_type: str, size: int) -> list:
    return list_of_hexa_colors(size) if color_type == "hexa" else list_of_rgb_colors(size)

#Exercises: Level 3
#3.1 Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
def shuffle_list(l: list) -> list:
    new_list = []
    original_size = len(l)
    for _ in range(0, original_size):
        i = randint(0, len(l)-1)
        new_list.append(l[i])
        l.pop(i)
    return new_list

#3.2 Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
def shuffle_seven_numbers() -> list:
    l = [0,1,2,3,4,5,6,7,8,9]
    new_list = []
    for _ in range(0, 7):
        i = randint(0, len(l)-1)
        new_list.append(l[i])
        l.pop(i)
    return new_list
