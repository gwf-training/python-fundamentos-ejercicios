#Exercises: Level 1
#Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. 
#If below 18 #give feedback to wait for the missing amount of years. Output:
edad = int(input("ingrese su edad: "))
if edad >= 18:
    print("tiene edad suficiente para conducir.")
else:
    print(f"Esperar los {18-edad} de años que faltan.")


#Compare the values of my_age and your_age using if … else. 
# Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. 
# You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences,
# and a custom text if my_age = your_age. Output:
mi_edad = 45
if (mi_edad > edad):
    print(f"Soy {mi_edad-edad} años mayor que tu")
elif(mi_edad < edad):
    print(f"Eres {edad-mi_edad} años mayor que yo")
else:
    print("tenemos la misma edad")

#Get two numbers from the user using input prompt. 
# If a is greater than b return a is greater than b, 
# if a is less b return a is smaller than b, else a is equal to b. Output:
a = int(input("ingrese un valor numerico para A: "))
b = int(input("ingrese un valor numerico para B: "))
if a > b: 
    print("A es mayor que B")
elif a < b:
    print("A es menor que B")
else:
    print("A es igual que B")

#Write a code which gives grade to students according to theirs scores:
#80-100, A
#70-89, B
#60-69, C
#50-59, D
#0-49, F
nota = int(input("ingrese la nota final del estudiante: "))
if nota <= 49:
    print("F")
elif nota <= 59:
    print("D")
elif nota <= 69:
    print("C")
elif nota <= 79:
    print("B")
else:
    print("A")


#Check if the season is Autumn, Winter, Spring or Summer. 
# If the user input is: September, October or November, 
# the season is Autumn. December, January or February, the season is Winter. March, April or May, t
# he season is Spring June, July or August, the season is Summer
mes = input("ingrese un mes: ").lower()
if mes in ["enero", "febrero", "marzo"]:
    print("VERANO")
elif mes in ["abril", "mayo", "junio"]:
    print("OTOÑO")
elif mes in ["julio","agosto","septiembre"]:
    print("INVIERNO")
elif mes in ["octubre", "noviembre", "diciembre"]:
    print("PRIMAVERA")
else:
    print("No ingresaste un mes valido")

#The following list contains some fruits:
#fruits = ['banana', 'orange', 'mango', 'lemon']
#If a fruit doesn't exist in the list add the fruit to the list and print the modified list. 
# If the fruit exists print('That fruit already exist in the list')
frutas = ['banana', 'naranja', 'mango', 'limon']
fruta = input("ingrese una fruta: ").lower()
if fruta not in frutas:
    frutas.append(fruta)
    print("frutas:", frutas)
else:
    print("la fruta ya existe en la lista")


#Exercises: Level 3
#Here we have a person dictionary. Feel free to modify it!
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    #'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    #'skills': ['JavaScript', 'React'],
    #'skills': ['Node', 'MongoDB', 'Python'],
    'skills': ['R', 'PowerBI', 'Office'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
# Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
skills = person.get("skills")
if "skills" in person:
    middle_skill = skills[len(skills)//2] 
    print("middle_skill:", middle_skill)

# Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if 'skills' in person and 'python' in skills:
    print("la persona tiene como skill python") 

# If a person skills has only JavaScript and React, print('He is a front end developer'), 
# if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
# if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'),
#  else print('unknown title') - for more accurate results more conditions can be nested!
skills_frontend = {'JavaScript', 'React'}
skills_backend = {'Node', 'MongoDB', 'Python'}
skills_fullstack = {'JavaScript', 'React', 'Node', 'MongoDB', 'Python'}
skills = set(person.get("skills")) 

is_front = len(skills - skills_frontend) == 0
print('is frontend:', is_front)


if skills == skills_frontend:
    print('He is a front end developer')
elif skills == skills_backend:
    print('He is a back end developer')
elif skills == skills_fullstack:
    print('He is a full stack developer')
else:
    print('unknown title')


# If the person is married and if he lives in Finland, print the information in the following format:
#   Asabeneh Yetayeh lives in Finland. He is married.
message = f"{person.get('first_name')} {person.get('last_name')} vive en Filandia. El esta casado"
print(message) if person.get('is_marred') and person.get('country')=='Finland' else print('Que paso aqui?')