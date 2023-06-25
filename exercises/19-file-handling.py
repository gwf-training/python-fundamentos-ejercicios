#Exercises: Level 1
#1. Write a function which count number of lines and number of words in a text. All the files are in the data the folder: 
# a) Read obama_speech.txt file and count number of lines and words
# b) Read michelle_obama_speech.txt file and count number of lines and words 
# c) Read donald_speech.txt file and count number of lines and words 
# d) Read melina_trump_speech.txt file and count number of lines and words
import re

def count_file_lines_and_words(f) -> tuple:
    speech_lines = f.read().splitlines()
    #words = set() # palabras unicas
    words = [] # todas la palabras
    for line in speech_lines:
        line = re.sub(r'[.,:;]', '',line)
        #words = words.union(set(line.split(' '))) #palabras unicas
        words = words + line.split(' ') # todas las palabras
    return len(speech_lines), len(words)

with open('./exercises/data/obama_speech.txt') as f:
    count_lines, count_words = count_file_lines_and_words(f)
    print("Obama speech lines:", count_lines)
    print("Obama speech words:", count_words)

with open('./exercises/data/michelle_obama_speech.txt') as f:
    count_lines, count_words = count_file_lines_and_words(f)
    print("Michelle Obama speech lines:", count_lines)
    print("Michelle Obama speech words:", count_words)

with open('./exercises/data/donald_speech.txt') as f:
    count_lines, count_words = count_file_lines_and_words(f)
    print("Donald Trump speech lines:", count_lines)
    print("Donald Trump speech words:", count_words)

with open('./exercises/data/melina_trump_speech.txt') as f:
    count_lines, count_words = count_file_lines_and_words(f)
    print("Melina Trump speech lines:", count_lines)
    print("Melina Trump speech words:", count_words)

#2. Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages
import json

languages = set()
with open('./exercises/data/countries_data.json') as f:
    countries = json.loads(f.read())
    for data in countries:
        languages = languages.union(set(data.get('languages')))
    print("number of languages:", len(languages))

#   3.2 Find the ten most spoken languages from the data
dict_languages = dict.fromkeys(languages, 0)
for data in countries:
    for lang in data.get('languages'):
        dict_languages[lang] =  dict_languages[lang] + 1

sorted_languages = sorted(dict_languages.items(), key=lambda x:x[1], reverse=True)
most_spoken_languages = dict(sorted_languages[:10])
print("most_spoken_languages:", most_spoken_languages)



#Read the countries_data.json data file in data directory, 
# create a function that creates a list of the ten most populated countries
def most_populated_countries(filename: str, topnumber: int) -> list:
    with open(filename) as f:
        countries = json.loads(f.read())
        countries_order_by_population = list(sorted(countries, key=lambda x:x['population'], reverse=True))[:topnumber]
        result = list()
        for country in countries_order_by_population:
            result.append( {
                "country": country.get('name'),
                "population": country.get('population')
            })
        return result 

# Your output should look like this
print('most_populated_countries:',most_populated_countries('./exercises/data/countries_data.json', 10))


#Exercises: Level 2
#Extract all incoming email addresses as a list from the email_exchange_big.txt file.
def clean_text_for_email(sentence: str) -> str:
    return re.sub(r'[$&#;!?<>,:()]', '',sentence)

def clean_text(sentence: str) -> str:
    return re.sub(r'[$&#;!?<>,:().]', '',sentence)


def get_uniques_words_10000(content: str) -> list:
    lines = content.splitlines()
    print("cantidad de lineas:", len(lines))
    words = set() # palabras unicas
    for line in lines[0:10000]: #limitacion para procesar menos lineas
        words = words.union(set(line.split(' '))) #palabras unicas
    return list(filter( lambda x: x != '', words))

def get_uniques_words(content: str) -> list:
    lines = content.splitlines()
    words = set() # palabras unicas
    for line in lines:
        words = words.union(set(line.split(' '))) #palabras unicas
    return list(filter( lambda x: x != '', words))

def get_mails(content: str) -> list:
    words = get_uniques_words_10000(content)
    print("cantidad de palabras unicas:", len(words))
    mails = []
    for word in words:
        is_email = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', word)
        if is_email is not None:
            mails.append(word)
    return mails

with open('./exercises/data/email_exchanges_big.txt') as f:
    content = clean_text_for_email(f.read())
    mails = get_mails(content)
    print("cantidad de mails:", len(mails))


# 2.2 Find the most common words in the English language. Call the name of your function find_most_common_words, 
# it will take two parameters - a string or a file and a positive integer, indicating the number of words. 
# Your function will return an array of tuples in descending order. Check the output
# Your output should look like this

def remove_support_words(words: list) -> list:
    words_to_remove = {'the', 'and', 'of', 'to', 'our', 'I', 'am', 'we', 'a', 'an', 'that', 'is', 'us', 'are', 'in', 'on'}
    new_words = []
    for word in words:
        if word not in words_to_remove:
            new_words.append(word)
    return new_words

def find_most_common_words(filename: str, topnumber: int) -> list:
    with open(filename) as f:
        content = clean_text(f.read())
        words = get_uniques_words(content)
        words = remove_support_words(words)
        words = list(filter( lambda x: x != '', words))
        dict_words = dict.fromkeys(words, 0)
        for word in words:
            dict_words[word] = len(re.findall(r'\b' + re.escape(word) + r'\b', content))
        return sorted(dict_words.items(), key=lambda x:x[1], reverse=True)[0:topnumber]


#Use the function, find_most_frequent_words to find: 
# a) The ten most frequent words used in Obama's speech 
result = find_most_common_words('./exercises/data/obama_speech.txt', 10)
print("Obama's speech: ", result)

# b) The ten most frequent words used in Michelle's speech 
result = find_most_common_words('./exercises/data/michelle_obama_speech.txt', 10)
print("Michelle's speech: ", result)

# c) The ten most frequent words used in Trump's speech 
result = find_most_common_words('./exercises/data/donald_speech.txt', 10)
print("Trump's speech: ", result)

# d) The ten most frequent words used in Melina's speech
result = find_most_common_words('./exercises/data/melina_trump_speech.txt', 10)
print("Melina's speech: ", result)

#Write a python application that checks similarity between two texts. 
# It takes a file or a string as a parameter and it will evaluate the similarity of the two texts. 
# For instance check the similarity between the transcripts of Michelle's and Melina's speech. 
# You may need a couple of functions, 
# function to clean the text(clean_text), 
# function to remove support words(remove_support_words) 
# and finally to check the similarity(check_text_similarity). 
# List of stop words are in the data directory


def get_words_relevance(filename: str) -> list:
    with open(filename) as f:
        content = clean_text(f.read())
        words = get_uniques_words(content)
        words = remove_support_words(words)
        return list(filter( lambda x: x != '', words))

def check_text_similarity(filename1: str, filename2: str) -> list:
    words_texto_1 = set(get_words_relevance(filename1))
    words_texto_2 = set(get_words_relevance(filename2))
    return list(words_texto_1.intersection(words_texto_2))

result = check_text_similarity('./exercises/data/michelle_obama_speech.txt', './exercises/data/melina_trump_speech.txt')
print('check_text_similarity:', len(result))

#Find the 10 most repeated words in the romeo_and_juliet.txt
result = find_most_common_words('./exercises/data/romeo_and_juliet.txt', 10)
print("romeo_and_juliet's: ", result)

#Read the hacker news csv file and find out: 
# a) Count the number of lines containing python or Python 
# b) Count the number lines containing JavaScript, javascript or Javascript 
# c) Count the number lines containing Java and not JavaScript
import csv

def count_lines(regex) -> int:
    with open('exercises/data/hacker_news.csv') as f:
        csv_reader = csv.reader(f, delimiter=',') # w use, reader method to read csv
        count = 0
        for row in csv_reader:
            if re.search(regex, row[1]) is not None:
                count += 1
    return count

print('python or Python:', count_lines(r'\b[Pp]ython\b'))
print('JavaScript, javascript or Javascript:',count_lines(r'\b[Jj]ava[Ss]cript\b'))
print('Java and not JavaScript:', count_lines(r'\b[Jj]ava\b(?![Ss]cript)'))
