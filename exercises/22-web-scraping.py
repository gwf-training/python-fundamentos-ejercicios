
#pip install requests
#pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup

url = 'https://archive.ics.uci.edu/dataset/791/metropt+3+dataset'

response = requests.get(url)
content = response.content # we get all the content from the website
soup = BeautifulSoup(content, 'html.parser') # beautiful soup will give a chance to parse
print("title:", soup.title) # <title>UCI Machine Learning Repository: Data Sets</title>
print("text:", soup.title.get_text()) # UCI Machine Learning Repository: Data Sets
#print(soup.body) # gives the whole page on the website
print("status code:",response.status_code)

tables = soup.find_all('table', {'class': 'my-4 table w-full'})
#print(tables)
# We are targeting the table with cellpadding attribute with the value of 3
# We can select using id, class or HTML tag , for more information check the beautifulsoup doc
table = tables[0] # the result is a list, we are taking out data from it
#print(table)
thead = table.find('thead')
tbody = table.find('tbody')
for th in thead.find('tr').find_all('th'):
    print(th.text)

for tr in tbody.find_all('tr'):
    print("-"*80)
    for td in tr.find_all('td'):
        print(td.text)

#Exercises
#1. Scrape the following website and store the data as json file
#  (url = 'http://www.bu.edu/president/boston-university-facts-stats/').

#2. Extract the table in this url (https://archive.ics.uci.edu/ml/datasets.php) and change it to a json file

#3. Scrape the presidents table and store the data as json 
#  (https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States). 
#  The table is not very structured and the scrapping may take very long time.