import requests

api_key = "c410ab4ea8b04e5c9934fd18399a6ecb"
url = ("https://newsapi.org/v2/everything?q=tesla&" \
       "from=2025-04-30&sortBy=publishedAt&" \
       "apiKey=c410ab4ea8b04e5c9934fd18399a6ecb")

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

#Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
