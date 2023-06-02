#Exercises: Level 1

#1. Create an empty tuple
brothers = tuple()
sisters = ()

#2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ("Hector", "Martin","Ariel", "Carlos", "Daniel")
sisters = ("Deysi", "Carina", "Francisca")

#3. Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters

#4. How many siblings do you have?
print("count: ", len(siblings))

#5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = list(siblings) + ["Ponciano", "Julia"]
print("family:",family_members)


#Exercises: Level 2
#1. Unpack siblings and parents from family_members
parents1, parents2, parents3, parents3, parents5, parents6, *rest_parents = family_members
print(parents1, parents2, parents3, parents3, parents5, parents6, rest_parents)

#2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ("banana", "naranja", "durazno", "frutilla", "wiki")
vegetables = ("papa", "tomate", "albahaca", "ajo", "peregil", "morron")
products = ("leche", "pan", "azucar", "fideos", "cerveza", "jugos")
food_stuff_tp = fruits + vegetables + products

#3. Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

#4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
idx = len(food_stuff_tp)//2
food_middle = food_stuff_tp[idx]
print("food_middle:", food_middle)

#5. Slice out the first three items and the last three items from food_staff_lt list
first_three = food_stuff_lt[:3]
print("first_three:",first_three)

last_three = food_stuff_lt[-3:]
print("first_three:",last_three)

#6. Delete the food_staff_tp tuple completely
del food_stuff_lt

#7. Check if an item exists in tuple:
exists_tomate = "tomate" in food_stuff_tp
print("exists tomate: ", exists_tomate)

#8. Check if 'Estonia' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
exists_estonia = "Estonia" in nordic_countries
print("exists estonia: ", exists_estonia)

#9. Check if 'Iceland' is a nordic country
exists_iceland = "Iceland" in nordic_countries
print("exists Iceland: ", exists_iceland)

#nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')