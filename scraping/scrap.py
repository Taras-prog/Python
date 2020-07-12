import requests
from bs4 import BeautifulSoup

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=40.71455000000003&lon=-74.00713999999994#.XwtXhCgzaM8')
soup = BeautifulSoup(page.content, 'html-parser')
print(soup)