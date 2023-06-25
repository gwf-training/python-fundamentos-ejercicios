#Exercises: Level 1
#1. Iterate 0 to 10 using for loop, do the same using while loop.
for i in range(11):
    print("for:",i)

i = 0
while i < 11:
    print("while:",i)
    i += 1



#2. Iterate 10 to 0 using for loop, do the same using while loop.
for i in list(range(11))[::-1]:
    print("for:",i)

i = 10
while i >= 0:
    print("while:",i)
    i -= 1

#3. Write a loop that makes seven calls to print(), so we get on the output the following triangle
for i in range(1,8):
    print("#"*i)

#4. Use nested loops to create the following:
for i in range(7):
    message = ""
    for j in range (7):
        message += "#"
    print(message)

#5. Print the following pattern:
#0 x 0 = 0
#1 x 1 = 1
#2 x 2 = 4
#3 x 3 = 9
#4 x 4 = 16
#5 x 5 = 25
#6 x 6 = 36
#7 x 7 = 49
#8 x 8 = 64
#9 x 9 = 81
#10 x 10 = 100
for i in range(11):
    print(f"{i} x {i} = {i*i}")

#6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
skills = ['Python', 'Numpy','Pandas','Django', 'Flask']
for skill in skills:
    print("skill:", skill)

#7. Use for loop to iterate from 0 to 100 and print only even numbers
for i in range(101):
    if i % 2 == 0:
        print("num:", i)

#8. Use for loop to iterate from 0 to 100 and print only odd numbers
for i in range(101):
    if i % 2 == 1:
        print("num:", i)

#Exercises: Level 2
#1. Use for loop to iterate from 0 to 100 and print the sum of all numbers.
#   The sum of all numbers is 5050.
sum = 0
for i in range(101):
    sum += i
print("The sum of all numbers is:", sum)

#Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
#   The sum of all evens is 2550. And the sum of all odds is 2500.
sum_evens = 0
sum_odds = 0
for i in range(101):
    if i % 2 == 0:
        sum_evens += i
    else:
        sum_odds += i
print("The sum of all numbers evens is:", sum_evens)
print("The sum of all numbers odds is:", sum_odds)

#1. Go to the data folder and use the countries.py file. 
# Loop through the countries and extract all the countries containing the word land.

from data.countries import countries

for country in countries:
    if "land" in country.lower():
        print("country:", country)

#2. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruits = ['banana', 'orange', 'mango', 'lemon']
i = len(fruits)-1
while i >=0:
    print(fruits[i])
    i -= 1

#3. Go to the data folder and use the countries_data.py file.
#   3.1 What are the total number of languages in the data
from data.countries_data import countries_data

languages = set()
for data in countries_data:
    languages = languages.union(set(data['languages']))
print("number of languages in the data:", len(languages))

#   3.2 Find the ten most spoken languages from the data
dict_languages = dict.fromkeys(languages, 0)
for data in countries_data:
    for lang in data['languages']:
        dict_languages[lang] =  dict_languages[lang] + 1
sorted_languages = sorted(dict_languages.items(), key=lambda x:x[1], reverse=True)
most_spoken_languages = dict(sorted_languages[:10])
print("most_spoken_languages:", most_spoken_languages)

#   3.3 Find the 10 most populated countries in the world
dict_countries = dict()
for data in countries_data:
    dict_countries[data.get('name')] = data.get('population')
sorted_populated_countries = sorted(dict_countries.items(), key=lambda x:x[1], reverse=True)
most_populated_countries = dict(sorted_populated_countries[:10])
print("most_populated_countries:", most_populated_countries)

sorted_populated_countries = sorted(countries_data, key=lambda x:x['population'], reverse=True)
most_populated_countries = sorted_populated_countries[:10]
for country in sorted_populated_countries[:10]:
    print(f"counttry={country.get('name')}, population={country.get('population')}")
