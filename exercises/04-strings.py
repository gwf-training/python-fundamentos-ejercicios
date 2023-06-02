
# ------------------------------------------
print("-"*100)
print('Exercises: strings')
print("-"*100)

#01. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
thirty, days, of, python = 'Thirty', 'Days', 'Of', 'Python'
print(thirty, days, of, python)

#02. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
coding, _for, _all = 'Coding', 'For' , 'All'
print(coding, _for, _all)

#03. Declare a variable named company and assign it to an initial value "Coding For All".
company = f"{coding} {_for} {_all}"

#04. Print the variable company using print().
print(company)

#05. Print the length of the company string using len() method and print().
print("len:", len(company))

#06. Change all the characters to uppercase letters using upper() method.
print("upper:", company.upper())

#07. Change all the characters to lowercase letters using lower() method.
print("lower:", company.lower())

#08. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print("capitalize:", company.capitalize())
print("tittle:", company.title())

#09. Cut(slice) out the first word of Coding For All string.
print("first word(slice):", company[:6])
print("first word(split):", company.split()[0])

#10. Check if Coding For All string contains a word Coding using the method index, find or other methods.
print("index(Coding):", company.index('Coding'))
print("find(Coding):", company.find('Coding'))

#11. Replace the word coding in the string 'Coding For All' to Python.
new_company = company.replace('Coding', 'Python')
print("replace:", new_company)

#12. Change Python for Everyone to Python for All using the replace method or other methods.
new_company = new_company.replace('Python', 'Everyone')
print("replace:", new_company)

#13. Split the string 'Coding For All' using space as the separator (split()) .
print("split:", company.split())

#14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
more_companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split()
print("more companies: ", more_companies)

#15. What is the character at index 0 in the string Coding For All.
print("index[0]: ", company[0])

#16. What is the last index of the string Coding For All.
print("lastindex: ", len(company)-1)
print("lastindex: ", company.rindex(company[-1]))

#17. What character is at index 10 in "Coding For All" string.
print("index[10]: ", company[10]) #space

#18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
new_company = company.replace('Coding', 'Python')
print("acronym: ", f"{new_company[0]}{new_company[7]}{new_company[11]}")
company_split = new_company.split()
print("acronym: ", f"{company_split[0][0]}{company_split[1][0]}{company_split[2][0]}")

#19. Create an acronym or an abbreviation for the name 'Coding For All'.
print("acronym: ", f"{company[0]}{company[7]}{company[11]}")

#20. Use index to determine the position of the first occurrence of C in Coding For All.
print("first ocurrence of C: ", company.index("C"))

#21. Use index to determine the position of the first occurrence of F in Coding For All.
print("first ocurrence of F: ", company.index("F"))

#22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
print("rfind last ocurrence of l: ", company.rindex("l"))

#23. Use index or find to find the position of the first occurrence of the word 'because' 
# in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
frase = 'You cannot end a sentence with because because because is a conjunction'
print("index for because:", frase.index("because"))

#24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print("rindex for because:", frase.rindex("because"))

#25. Slice out the phrase 'because because because' in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'
new_frase = 'You cannot end a sentence with because because because is a conjunction'
new_frase_slice = new_frase[new_frase.index('because'):new_frase.rindex('because')+7]
print("slice:", new_frase_slice)

#26. Find the position of the first occurrence of the word 'because' in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'
print("first ocurrence because:", new_frase.index('because'))

#27. Slice out the phrase 'because because because' in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'
new_frase = 'You cannot end a sentence with because because because is a conjunction'
new_frase_slice = new_frase[new_frase.index('because'):new_frase.rindex('because')+7]
print("slice:", new_frase_slice)

#28. Does ''Coding For All' start with a substring Coding?
print("replace:", company.replace('Coding', 'Coding?'))

#29. Does 'Coding For All' end with a substring coding?
print("end with:", company + " coding") 

#30. '   Coding For All      '  , remove the left and right trailing spaces in the given string.
text = '   Coding For All      '
print("remove spaces: ", text.replace(' ', ''))

#31. Which one of the following variables return True when we use the method isidentifier():
#   30DaysOfPython
#   thirty_days_of_python
print("isidentifier(30DaysOfPython): ", "30DaysOfPython".isidentifier())
print("isidentifier(thirty_days_of_python): ", "thirty_days_of_python".isidentifier())

#32. The following list contains the names of some of python libraries: 
# ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libreries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print("join:", " ".join(libreries))

#33. Use the new line escape sequence to separate the following sentences.
#   I am enjoying this challenge.
#   I just wonder what is next.
new_line = "I am enjoying this challenge.\nI just wonder what is next."
print(new_line)

#34. Use a tab escape sequence to write the following lines.
#   Name      Age     Country   City
#   Asabeneh  250     Finland   Helsinki
new_line = "Name\t\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki"
print(new_line)

#35. Use the string formatting method to display the following:
#   radius = 10
#   area = 3.14 * radius ** 2
#   The area of a circle with radius 10 is 314 meters square.
print("radius = {}".format(10))
print("area = {} * radius ** {}".format(3.14,2))
print("The area of a circle with radius {} is {} meters square.".format(10, 314))

#36. Make the following using string formatting methods:
#   8 + 6 = 14
#   8 - 6 = 2
#   8 * 6 = 48
#   8 / 6 = 1.33
#   8 % 6 = 2
#   8 // 6 = 1
#   8 ** 6 = 262144

num1 = 8
num2 = 6
print(f"{num1} + {num2} = {num1+num2}")
print(f"{num1} - {num2} = {num1-num2}")
print(f"{num1} * {num2} = {num1*num2}")
print(f"{num1} / {num2} = {(num1/num2):.2f}")
print(f"{num1} % {num2} = {num1%num2}")
print(f"{num1} // {num2} = {num1//num2}")
print(f"{num1} ** {num2} = {num1**num2}")
