# Exercises: Level 1
print('-'*100)
print("Exercises: Level 1")
print('-'*100)

# 1. Declare an empty list
paises = list()

# 2. Declare a list with more than 5 items
paises = ["argentia", "uruguay", "brasil", "francia", "portugal"]
print("paises:", paises)

# 3. Find the length of your list
print("len:", len(paises))

# 4. Get the first item, the middle item and the last item of the list
print("paises [first,middle,last]: ", paises[0], paises[2], paises[4])

# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["Gustavo", 45, 1.67, "casado", "learning", "Belsky 1132"]
print("mixed_data_types:", mixed_data_types)

# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# 7. Print the list using print()
print("it_companies:", it_companies)

# 8. Print the number of companies in the list
print("len:", len(it_companies))

# 9. Print the first, middle and last company
print("it_companies [first,middle,last]: ", it_companies[0], it_companies[3], it_companies[6])

# 10. Print the list after modifying one of the companies
it_companies[0] = "OpenIA"
print("it_companies:", it_companies)

# 11. Add an IT company to it_companies
it_companies.append("Spotify")
print("it_companies:", it_companies)

# 12. Insert an IT company in the middle of the companies list
it_companies.insert(3, "Netflix")
print("it_companies:", it_companies)

# 13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[7] = it_companies[7].upper()
print("it_companies:", it_companies)

# 14. Join the it_companies with a string '#;  '
print("join companies:", "#; ".join(it_companies))

# 15. Check if a certain company exists in the it_companies list.
print("exist Apple: ", "Apple" in it_companies)
print("exist Adidas: ", "Adidas" in it_companies)

# 16. Sort the list using sort() method
# it_companies.sort()
# print("sort:", sorted(it_companies, reverse=True))
print("sort:", sorted(it_companies))

# 17. Reverse the list in descending order using reverse() method
it_companies.reverse()
print("reverse:", it_companies)

# 18. Slice out the first 3 companies from the list
firts_3 = it_companies[0:3]
print("firts_3:", firts_3)

# 19. Slice out the last 3 companies from the list
last_3 = it_companies[-3: len(it_companies)]
print("last_3:", last_3)

# 20. Slice out the middle IT company or companies from the list
middle = it_companies[len(it_companies)//2]
print("middle:", middle)

# 21. Remove the first IT company from the list
c = it_companies.pop(0)
print("it_companies:", it_companies, c)

# 22. Remove the middle IT company or companies from the list
del it_companies[len(it_companies)//2]
print("it_companies:", it_companies)

# 23. Remove the last IT company from the list
c = it_companies.pop()
print("it_companies:", it_companies, c)

# 24. Remove all IT companies from the list
it_companies.clear()
print("clear:", it_companies)

# 25. Destroy the IT companies list
del it_companies
# print("del:", it_companies)

# 26. Join the following lists:
#   front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
#   back_end = ['Node','Express', 'MongoDB']
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
fullstack = front_end + back_end
print("fullstack:", fullstack)

# 27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack.
# Then insert Python and SQL after Redux.
fullstack.insert(fullstack.index('Redux')+1, 'Python')
fullstack.insert(fullstack.index('Redux')+1, 'SQL')
print("fullstack:", fullstack)


# Exercises: Level 2
print('-'*100)
print("Exercises: Level 2")
print('-'*100)

# The following is a list of 10 students ages:
# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print("ages:", ages)

# 1. Sort the list and find the min and max age
ages.sort()
print("sort:", ages)
minimo = min(ages)
maximo = max(ages)
print(f"min: {minimo}, max: {maximo}")

# 2. Add the min age and the max age again to the list
ages.append(minimo)
ages.append(maximo)
print("ages:", ages)

# 3. Find the median age (one middle item or two middle items divided by two)
print("edad media:", minimo+(maximo-minimo)/2)

# 4. Find the average age (sum of all items divided by their number )
edad_promedio = sum(ages) / len(ages)
print("edad media:", edad_promedio)

# 5. Find the range of the ages (max minus min)
rango_edad = maximo-minimo
print("rango_edad:", rango_edad)

# 6. Compare the value of (min - average) and (max - average), use abs() method
print("(min - average)", abs(minimo - edad_promedio))
print("(max - average)", abs(maximo - edad_promedio))

# 7. Find the middle country(ies) in the countries list
print("pais middle:", paises[len(paises)//2])

# Divide the countries list into two equal lists if it is even if not one more country for the first half.
# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark'].
# Unpack the first three countries and the rest as scandic countries.
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
china, russia, usa, *rest = countries
print(china, russia, usa, rest)
