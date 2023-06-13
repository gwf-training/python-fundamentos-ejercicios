#Por ejemplo, si desea cambiar una cadena a una lista de caracteres. Puedes usar un par de métodos:
# One way
language = 'Python'
lst = list(language) # changing the string to list
print(type(lst))     # list
print(lst)           # ['P', 'y', 't', 'h', 'o', 'n']

# Second way: list comprehension
lst = [i for i in language]
print(type(lst)) # list
print(lst)       # ['P', 'y', 't', 'h', 'o', 'n']

#For instance if you want to generate a list of numbers
# Generating numbers
numbers = [i for i in range(11)]  # to generate numbers from 0 to 10
print(numbers) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# It is possible to do mathematical operations during iteration
squares = [i * i for i in range(11)]
print(squares) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# It is also possible to make a list of tuples
numbers = [(i, i * i) for i in range(11)]
print(numbers) # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

# Generating even numbers
even_numbers = [i for i in range(21) if i % 2 == 0]  # to generate even numbers list in range 0 to 21
print(even_numbers)                    # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Generating odd numbers
odd_numbers = [i for i in range(21) if i % 2 != 0]  # to generate odd numbers in range 0 to 21
print(odd_numbers)                      # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# Filter numbers: let's filter out positive even numbers from the list below
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in range(21) if i % 2 == 0 and i > 0]
print(positive_even_numbers)                    # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Flattening a three dimensional array
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [ number for row in list_of_lists for number in row]
print(flattened_list)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]



#
#Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
result = [i for i in numbers if i <=0]
print("only negative and zero", result)

#Flatten the following list of lists of lists to a one dimensional list :
#output [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
result = [col for l in list_of_lists for row in l for col in row]
print("one dimensional list:",result)

#Using list comprehension create the following list of tuples:
#[(0, 1, 0, 0, 0, 0, 0),
#(1, 1, 1, 1, 1, 1, 1),
#(2, 1, 2, 4, 8, 16, 32),
#(3, 1, 3, 9, 27, 81, 243),
#(4, 1, 4, 16, 64, 256, 1024),
#(5, 1, 5, 25, 125, 625, 3125),
#(6, 1, 6, 36, 216, 1296, 7776),
#(7, 1, 7, 49, 343, 2401, 16807),
#(8, 1, 8, 64, 512, 4096, 32768),
#(9, 1, 9, 81, 729, 6561, 59049),
#(10, 1, 10, 100, 1000, 10000, 100000)]
def power(x):
    return lambda n : x ** n

result = [ (i, i**0,i**1,i**2,i**3) for i in range(11)]
for t in result:
    print(t)

#Flatten the following list to a new list:
#output:[['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
result = [  [i[0].upper(),i[0].upper()[0:3],i[1].upper()] for row in countries for i in row]
for t in result:
    print(t)
