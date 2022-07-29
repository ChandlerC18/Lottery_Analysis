import requests
from bs4 import BeautifulSoup
import pandas as pd


# Create new dataframe
df = pd.DataFrame(columns=['Date', 'Ball 1', 'Ball 2', 'Ball 3', 'Ball 4', 'Ball 5', 'Mega ball', 'Megaplier'])

for i in range(1996, 2023):
    print(i) # print year
    
    # Making a GET request
    # r = requests.get('https://www.megamillions.com/Winning-Numbers/Previous-Drawings.aspx')
    r = requests.get(f'https://www.nylottery.org/mega-millions/past-winning-numbers/{i}')

    # check status code for response received
    # success code - 200

    # Parsing the HTML
    soup = BeautifulSoup(r.content, 'html.parser')
    content = soup.find_all('td', class_='centred')

    # loop through and save data to dataframe
    for j in range(len(content) - 1, -1, -3):
        date = content[j - 2].text.split('\n')
        numbers = content[j - 1].text.split('\n')
        megaplier = numbers[7].split(' ')[1] if numbers[7] != '' else ''
        df.loc[len(df.index)] = [date[1], numbers[1], numbers[2], numbers[3], numbers[4], numbers[5], numbers[6], megaplier]

df.to_csv('lottery_data.csv')
print(df)
