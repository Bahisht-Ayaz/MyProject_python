import pandas
import requests
from bs4 import BeautifulSoup

web_url = "https://luckyone.com.pk/shopping/"
response = requests.get(web_url)
print(response)