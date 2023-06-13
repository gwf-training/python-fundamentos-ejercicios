def power(x):
    return lambda n : x ** n

cube = power(2)   # function power now need 2 arguments to run
print("type cube:", type(cube))
print(cube(3))          # 8

cube = power(2)(3)   # function power now need 2 arguments to run, in separate rounded brackets
print(cube)          # 8
two_power_of_five = power(2)(5) 
print(two_power_of_five)  # 32


#5. Change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
#output:
#[{'country': 'FINLAND', 'city': 'HELSINKI'},
#{'country': 'SWEDEN', 'city': 'STOCKHOLM'},
#{'country': 'NORWAY', 'city': 'OSLO'}]

map_to_dic = lambda l: {'country': l[0].upper(), 'city': l[1].upper()}
result = [  map_to_dic(i) for row in countries for i in row]
for t in result:
    print(t)

#Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
#output ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
result = [name for row in names for col in row for name in col]
print(result)


#Write a lambda function which can solve a slope or y-intercept of linear functions. TODO