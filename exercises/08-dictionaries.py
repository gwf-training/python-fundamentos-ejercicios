person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}


#Exercises: Day 8
#1. Create an empty dictionary called dog
dog = dict()
print("type dog:", type(dog))

#2. Add name, color, breed, legs, age to the dog dictionary
dog = {
    "name": "Blacky", 
    "color": "black", 
    "breed": "callejero", 
    "legs": 4, 
    "age": 3
}
print("dog:", dog)

#3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address 
# as keys for the dictionary
student = {
    'first_name': 'Ricardo',
    'last_name': 'Cardetti',
    'gender': 'hombre',
    'age': 25,
    'marital_status': 'divorciado',
    'country': 'Argentina',
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'city': 'Merlo',
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
print("student:", student)

#4. Get the length of the student dictionary
print("len:", len(student))

#5. Get the value of skills and check the data type, it should be a list
has_java_skill = "java" in student.get('skills')
print("has_java_skill:", has_java_skill)
has_python_skill = "Python" in student.get('skills')
print("has_python_skill:", has_python_skill)

#6. Modify the skills values by adding one or two skills
student.get('skills').append('Go')
student.get('skills').append('Rust')
print('skills:', student.get('skills'))

#7. Get the dictionary keys as a list
print('keys:', student.keys())

#8. Get the dictionary values as a list
print("values:", student.values())

#9. Change the dictionary to a list of tuples using items() method
print("to list:", list(student.items()))


#10. Delete one of the items in the dictionary
student.pop('address')
print("student:", student.keys())

#11. Delete one of the dictionaries
student.popitem()
print("student:", student.keys())
