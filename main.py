import requests
from send_email import send_email

topic = "tesla"

api_key = "c410ab4ea8b04e5c9934fd18399a6ecb"
url = "https://newsapi.org/v2/everything?"\
       f"q={topic}&"\
       "sortBy=publishedAt&"\
       "apiKey=c410ab4ea8b04e5c9934fd18399a6ecb&"\
       "language=en"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

body = ""

for article in content["articles"][:20]:
    if article["title"] is not None and article["description"] is not None:
        body = "Subject: Today news" + "\n" + (body + article["title"] + "\n"\
                + article["description"] \
                + "\n" + article["url"] + "\n\n")

body = body.encode("utf-8")
send_email(body)
