import re

## MATCH
txt = 'I love to 1 teach python and javaScript'
# It returns an object with span, and match
match = re.match('I love to teach', txt, re.I)
print(match)  # <re.Match object; span=(0, 15), match='I love to teach'>
# We can get the starting and ending position of the match as tuple using span
if match != None:
    span = match.span()
    print(span)     # (0, 15)
    # Lets find the start and stop position from the span
    start, end = span
    substring = txt[start:end]
    print(substring)       # I love to teach
else:
    print('la cadena de texto no comienza con el patron indicado')

## SEARCH
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''
# It returns an object with span and match
search = re.search('first', txt, re.I)
print(search)  # <re.Match object; span=(100, 105), match='first'>
# We can get the starting and ending position of the match as tuple using span
if search != None:
    span = search.span()
    print(span)     # (100, 105)
    # Lets find the start and stop position from the span
    start, end = span
    substring = txt[start:end]
    print(substring)       # first

## FIND ALL
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It return a list
matches = re.findall('language', txt, re.I)
print(matches)  # ['language', 'language']
matches = re.findall('Python|python', txt)
print(matches)  # ['Python', 'python']
matches = re.findall('[Pp]ython', txt)
print(matches)  # ['Python', 'python']


txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'[^A-Za-z ]+'  # ^ in set character means negation, not A to Z, not a to z, no space
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6,', '2019', '8', '2021']



########################
#Exercises: Level 1
#1. What is the most frequent word in the following paragraph?

def most_frequent_words(paragraph: str) -> list :
    new_paragraph = re.sub(r'[\.,]','',paragraph)
    words = re.split(' ', new_paragraph)
    dict_words = dict.fromkeys(words, 0)
    for word in words:
        dict_words[word] = dict_words[word] + 1
    return sorted(dict_words.items(), key=lambda x:x[1], reverse=True)

def most_frequent_word_with_re(paragraph: str) -> list:
    new_paragraph = re.sub(r'[\.,]','',paragraph)
    words = set(re.split(' ', new_paragraph))
    dict_words = dict.fromkeys(words, 0)
    for word in words:
        dict_words[word] = len(re.findall(r'\b' + re.escape(word) + r'\b', new_paragraph))
    return sorted(dict_words.items(), key=lambda x:x[1], reverse=True)

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
print("most_frequent_words:", most_frequent_words(paragraph))
print("most_frequent_word_with_re:", most_frequent_word_with_re(paragraph))

#2. The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.
points = ['-1', '2', '-4', '-3', '-1', '0', '4', '8']
sorted_points =  [-4, -3, -1, -1, 0, 2, 4, 8]
#distance = 8 -(-4) # 12
#TODO

#Exercises: Level 2
#Write a pattern which identifies if a string is a valid python variable
def is_valid_variable(name: str) -> bool:
    regex = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    return re.match(regex, name) is not None

print("is_valid_variable: ", is_valid_variable('first_name')) # True
print("is_valid_variable: ", is_valid_variable('first-name')) # False
print("is_valid_variable: ", is_valid_variable('1first_name')) # False
print("is_valid_variable: ", is_valid_variable('firstname')) # True

#Exercises: Level 3
#Clean the following text. After cleaning, count three most frequent words in the string.
def clean_text(sentence: str) -> str:
    return re.sub(r'[%@$&#;!?]', '',sentence)

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
cleaned_text = clean_text(sentence)
print("cleaned_text:",cleaned_text);
#I am a teacher and I love teaching There is nothing as more rewarding as educating and empowering people I found teaching more interesting than any other jobs Does this motivate you to be a teacher
print("most_frequent_words: ",most_frequent_words(cleaned_text)) # [(3, 'I'), (2, 'teaching'), (2, 'teacher')]