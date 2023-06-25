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

  