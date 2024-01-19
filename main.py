import requests
import os


api_key = os.getenv("APIKEY")
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-12-19&sortBy=publishedAt&apiKey=" + api_key
# Make requests
request = requests.get(url=url)

# Get a dictionary with data
content = request.json()

# get articles with description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
