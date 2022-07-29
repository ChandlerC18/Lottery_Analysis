import requests
from bs4 import BeautifulSoup

# Making a GET request
r = requests.get('https://www.megamillions.com/Winning-Numbers/Previous-Drawings.aspx')

# check status code for response received
# success code - 200
print(r)

# print content of request
print(r.content)

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())
