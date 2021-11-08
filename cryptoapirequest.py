import requests
import json
import time
import os
from google.colab import files

url_base = "https://api.nomics.com/v1/exchange-rates/history?key=a5f6bdc7628462a323f7f92f0655fd8c21edb27b&currency={}&start=2018-04-14T00%3A00%3A00Z&end=T00%3A00%3A00Z"

# NOW PICK ALL THE SERIES THAT WE ARE INTERESTED IN:
fredSeries = ['BTC', 'ETH', 'SOL', 'BNB']

# // Begin a loop, dealing with series one by one:
for i in fredSeries:  
   # // Build the URL for this iteration of the loop, and check what we are getting:
   URL = url_base.format(i)
   print(URL)

   data = requests.get(URL).json()

   fileName = "data_rate_"+str(i)+".json"
   print(fileName)

   with open(fileName, 'w', encoding='utf-8') as f:
     json.dump(data, f, ensure_ascii=False, indent=4)

   files.download('{}'.format(fileName))
  
