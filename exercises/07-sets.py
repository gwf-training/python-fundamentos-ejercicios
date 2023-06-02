#1. Find the length of the set it_companies
it_companies = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}
print("length:", len(it_companies))

#2. Add 'Twitter' to it_companies
it_companies.add("Twitter")
print("it_companies:", it_companies)

#3. Insert multiple IT companies at once to the set it_companies
it_companies.update(["Alphabet Inc", "Oracle", "SAP", "Uber", "Atlassian"])
print("it_companies:", it_companies)

#4. Remove one of the companies from the set it_companies
it_companies.remove("Uber")
print("it_companies:", it_companies)

#5. What is the difference between remove and discard
it_companies.discard("SAP")
#it_companies.remove("SAP") #Da un error porque no existe el elemento a eliminar
print("it_companies:", it_companies)


#Exercises: Level 2
#1. Join A and B
a = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}
b = {"Alphabet Inc", "Apple","Oracle", "SAP", "Uber", "Atlassian", "Google"}
c = {"Apple","Oracle", "Google"}
d = {"Facebook","Microsoft"}
print("union:", a.union(b))

#2. Find A intersection B
print("intersection:",a.intersection(b))

#3. Is A subset of B
print("issubset:", a.issubset(b))
print("issubset:", c.issubset(b))

#4. Are A and B disjoint sets
print("isdisjoint:", a.isdisjoint(b))
print("isdisjoint:", c.isdisjoint(d))

#5. Join A with B and B with A
print("union:", a.union(b))
print("union:", b.union(a))

#6. What is the symmetric difference between A and B
print("symmetric_difference:", a.symmetric_difference(b))

#7. Delete the sets completely
del a
del b

#Exercises: Level 3
#1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
ages_lt = [11, 49, 45, 8, 30, 8]
ages_st = set(ages_lt)

print("len list:", len(ages_lt))
print("len set:", len(ages_st)) 

#2. Explain the difference between the following data types: string, list, tuple and set
#LIST: es una coleccion de datos ordenados y mutables
#TUPLE: es una coleccion de datos ordenados y inmutables
#SET: es una coleccion de datos no ordenada, no indexada y no admite repetidos

#I am a teacher and I love to inspire and teach people. 
# How many unique words have been used in the sentence? 
# Use the split methods and set to get the unique words.
texto = "I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words."
texto = texto.replace("?", "")
texto = texto.replace(".", "")
all_words = texto.split()
#print("all words:", all_words)
print("unique words", set(all_words))