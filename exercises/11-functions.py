# 1. Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(a: int, b: int) -> int:
    return a + b


print("add_two_numbers:", add_two_numbers(5, 8))

# 2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.


def area_of_circle(radio: float) -> float:
    PI = 3.14
    return PI * radio * radio


print("area_of_circle:", area_of_circle(2))

# 3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments.
# Check if all the list items are number types. If not do give a reasonable feedback.


def add_all_nums(*numbers: int) -> int:
    result = 0
    for number in numbers:
        result += number
    return result


print("add_all_nums:", add_all_nums(1, 2, 3, 4, 5, 6))

# 4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32.
# Write a function which converts °C to °F, convert_celsius_to-fahrenheit.


def convert_celsius_to_fahrenheit(celsius: float) -> float:
    return (celsius * 9 / 5) + 32


print("convert_celsius_to_fahrenheit:", convert_celsius_to_fahrenheit(37))

# 5. Write a function called check-season, it takes a month parameter and
# returns the season: Autumn, Winter, Spring or Summer.


def check_season(month: str) -> str:
    season = ""
    if month in ["enero", "febrero", "marzo"]:
        season = "VERANO"
    elif month in ["abril", "mayo", "junio"]:
        season = "OTOÑO"
    elif month in ["julio", "agosto", "septiembre"]:
        season = "INVIERNO"
    elif month in ["octubre", "noviembre", "diciembre"]:
        season = "PRIMAVERA"
    return season


print("check_season:", check_season('mayo'))

# 6. Write a function called calculate_slope which return the slope of a linear equation
# def calculate_slope(slope) TODO

# 7. Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
# def solve_quadratic_eqn() TODO

# 8. Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
nombres = ['juan', 'pedro', 'luis', 'pepe']
def print_list(params):
    for p in params:
        print('param:', p)

print_list(nombres)

# 9. Declare a function named reverse_list. It takes an array as a parameter
# and it returns the reverse of the array (use loops).
def reverse_list(params):
    i = len(params)-1
    new_list = []
    while i >= 0:
        new_list.append(params[i])
        i -= 1
    return new_list

print("reverse_list:", reverse_list(nombres))
print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(["A", "B", "C"]))

#10. Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(params):
    items = []
    for param in params:
        items.append(param.capitalize())
    return items
print("capitalize_list_items:", capitalize_list_items(nombres))

#11. Declare a function named add_item. It takes a list and an item parameters. 
# It returns a list with the item added at the end.
def add_item(items, item):
    items.append(item)
    return items

print("add_item:", add_item(nombres, 'willy'))
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9];
print(add_item(numbers, 5))      # [2, 3, 7, 9, 5]

#12. Declare a function named remove_item. It takes a list and an item parameters. 
# It returns a list with the item removed from it.
def remove_item(items, item):
    items.remove(item)
    return items

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9];
print(remove_item(numbers, 3))  # [2, 7, 9]

#13. Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(num: int) -> int:
    sum = 0
    for i in range(1, num+1):
        sum += i
    return sum

print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050

#14. Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(to: int) -> int:
    sum = 0
    for number in range (1, to+1):
        if number % 2 == 1:
            sum += number
    return sum
print("sum_of_odds:", sum_of_odds(10))

#15. Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range
def sum_of_evens(to: int) -> int:
    sum = 0
    for number in range (1, to+1):
        if number % 2 == 0:
            sum += number
    return sum
print("sum_of_evens:", sum_of_evens(10))

#Exercises: Level 2
#1. Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
    #print(evens_and_odds(100))
    # The number of odds are 50.
    # The number of evens are 51.
def evens_and_odds(to: int):
    count_odds = 0
    count_evens = 0
    for number in range(1, to+1):
        if number % 2 == 0:
            count_evens += 1
        else:
            count_odds += 1
    return (count_evens, count_odds)

print(evens_and_odds(100))

#2. Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(number: int) -> int:
    if number == 1:
        return 1
    else:
        return factorial(number-1) * number
print("factorial:",factorial(7))

#3. Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(param) -> bool:
    return (param == "" or param == None)
name = 'Juan'
print("is_empty:", is_empty(name))
name = None
print("is_empty:", is_empty(name))

#4. Write different functions which take lists. They should calculate_mean, calculate_median, 
# calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
def calculate_mean(numbers) -> float:
    sum_numbers = 0
    count_numbers = 0
    for num in numbers:
        sum_numbers += num
        count_numbers += 1
    print(sum_numbers, count_numbers)
    return sum_numbers/count_numbers
numbers = [10, 2, 3, 5, 7,3]
print("calculate_mean:", calculate_mean(numbers))


def calculate_median(numbers) -> float:
    new_numbers = sorted(numbers)
    middle = len(numbers) // 2
    if len(numbers) % 2 == 1:
        return new_numbers[middle]
    else:
        a = new_numbers[middle-1]
        b = new_numbers[middle]
        return (a+b)/2

print("calculate_median:", calculate_median([2,2,3,7,8,9,9]))
print("calculate_median:", calculate_median(numbers))

#Para encontrar el rango, restamos el valor mínimo del conjunto de datos del valor máximo. 
#Por ejemplo, en los datos de 2, 5, 3, 4, 5, y 5, el valor mínimo es 2 y el valor máximo es 5, 
#entonces el rango es 5 – 2, o 3.
def calculate_range(numbers):
    min_value = min(numbers)
    max_value = max(numbers)
    return max_value-min_value

print("calculate_range", calculate_range(numbers))

#def calculate_variance(numbers) TODO
#def calculate_std(number) TODO

#Exercises: Level 3
#3.1 Write a function called is_prime, which checks if a number is prime.
#def id_prime (number: int) -> bool:
    
#3.2 Write a functions which checks if all items are unique in the list.
#3.3 Write a function which checks if all the items of the list are of the same data type.
#3.4 Write a function which check if provided variable is a valid python variable
#3.5 Go to the data folder and access the countries-data.py file.

#3.6 Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
#3.7 Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.