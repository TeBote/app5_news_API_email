import requests
from send_email import send_email

api_key = "c410ab4ea8b04e5c9934fd18399a6ecb"
url = ("https://newsapi.org/v2/everything?q=tesla&"\
       "sortBy=publishedAt&"\
       "apiKey=c410ab4ea8b04e5c9934fd18399a6ecb")

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

body = ""

for article in content["articles"]:
    if article["title"] is not None and article["description"] is not None:
        body = body + article["title"] + "\n" + article["description"] + "\n\n"

body = body.encode("utf-8")
send_email(body)


