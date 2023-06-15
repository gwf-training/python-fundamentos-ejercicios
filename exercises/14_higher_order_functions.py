from functools import reduce

numbers_str = ['1', '2', '3', '4', '5']  # iterable
def add_two_nums(x, y):
    print(x, y)
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str)
print(total)    # 15

#Exercises: Level 1
#1.1 Explain the difference between map, filter, and reduce.
#map: se utilizan para transformar valores de un iterable
#filter: se utiliza para filtrar elemento de un iterable
#reduce: se utilizar para recorrer un iterable y obtener un unico valor, por cada iteracion la invocacion 
# a la funcion se realiza con 2 valores, un acumulador y el valor actual de la iteracion

#1.2 Explain the difference between higher order function, closure and decorator
#higher order function: tiene las siguientes caracteristicas
# - las funciones pueden recibir funciones como parametros
# - las funciones pueden retornar funciones
# - las funciones se puede asignar a variables
# - las funciones se pueden modificar/extender
#closure: permiter a una funcion anidada acceder al ambito externo de su funcion envolvente
#decorator: son funciones que extienden el funcionamiento actual de una funncion sin modificar su estructura.

#1.3 Define a call function before map, filter or reduce, see examples.
numbers = [1,2,3,4,5,6,7,8,9,10]
print("numbers:", numbers)
square_numbers = map(lambda n: n*n, numbers)
print("square_numbers:", list(square_numbers))
even_numbers = filter(lambda n: n%2==0,numbers)
print("even_numbers:", list(even_numbers))
sum_numbers = reduce(lambda acumulador, number: acumulador+number,numbers)
print("sum_numbers:", sum_numbers)

#1.4 Use for loop to print each country in the countries list.
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway','Denmark']
def print_list(l: list):
    for element in l: print(element)

print_list(countries)

#1.5 Use for to print each name in the names list.
names = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print_list(names)

#Use for to print each number in the numbers list.
print_list(numbers)

#Exercises: Level 2
#2.1 Use map to create a new list by changing each country to uppercase in the countries list
upper_countries = map(lambda country: country.upper(), countries)
print("upper_countries:", list(upper_countries))

#2.2 Use map to create a new list by changing each number to its square in the numbers list
square_numbers = map(lambda n: n*n, numbers)
print("square_numbers:", list(square_numbers))

#2.3 Use map to change each name to uppercase in the names list
upper = lambda name: name.upper()
upper_names = map(lambda name: name.upper(), names)
print("upper_names:", list(upper_names))

#2.4 Use filter to filter out countries containing 'land'.
result = filter(lambda country: "land" in country, countries)
print("countries containing land:", list(result))

#2.5 Use filter to filter out countries having exactly six characters.
def havingLen(size:int ):
    return lambda country: len(country)==size
def havingLenOrMore(size:int ):
    return lambda country: len(country)>=size

result = filter(havingLen(6), countries)
print("countries having six characters.:", list(result))

#2.6 Use filter to filter out countries containing six letters and more in the country list.
result = filter(lambda country: len(country)>=6, countries)
print("countries containing six letters and more:", list(result))

#2.7 Use filter to filter out countries starting with an 'E'
result = filter(lambda country: country[0]!='U', countries)
print("filter out countries starting with an 'U':", list(result))

#2.8 Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
result = reduce(lambda x, y: x+y, map(lambda c: len(c), filter(havingLenOrMore(6), countries)))
print("Chain two or more list iterators:", result)

#2.9 Declare a function called get_string_lists which takes a list as a parameter and then 
# returns a list containing only string items.
def get_string_lists(l: list) -> list:
    return list(filter(lambda e: isinstance(e,str), l))
    #return list(filter(lambda e: type(e)==str, l))

print(get_string_lists([1, "juan", True, 'independiente']))

#2.10 Use reduce to sum all the numbers in the numbers list.
result = reduce(lambda x,y: x+y, numbers)
print("sum all the numbers:", result)

#2.11 Use reduce to concatenate all the countries and to produce this sentence: 
# Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European 
north_european = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

def new_reduce(l: list):
    last_element = l[-1]
    return reduce(lambda x, y:  x + ', ' + y if y != last_element else x + ' and ' + y, l)

print("north_european:", new_reduce(north_european))


#2.12 Declare a function called categorize_countries that returns a list of countries 
# with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
#TODO

#2.13 Create a function returning a dictionary, where keys stand for starting letters 
# of countries and values are the number of country names starting with that letter.
#TODO

#2.14 Declare a get_first_ten_countries function - it returns a list of first ten countries
#  from the countries.js list in the data folder.
#TODO

#2.15 Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
#TODO

#Exercises: Level 3
#Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:
#Sort countries by name, by capital, by population
#Sort out the ten most spoken languages by location.
#Sort out the ten most populated countries.
#TODO