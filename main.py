import requests
import os
from send_email import send_email

api_key = os.getenv("APIKEY")
topic = "tesla"
url = (("https://newsapi.org/v2/everything?"
        f"q={topic}&from=2023-12-19"
        "&sortBy=publishedAt&apiKey=") + api_key +
       "&language=en")
# Make requests
request = requests.get(url=url)

# Get a dictionary with data
content = request.json()

body = ""
# get articles with description
for article in content["articles"][:20]:
    if article["title"] is not None and article["description"] is not None:
        body = ("Subject: Today's News" + "\n" + body + article["title"] +
                "\n" + article["description"] + "\n" + article["url"] + 2 * "\n")

body = body.encode("utf-8")
send_email(body)
