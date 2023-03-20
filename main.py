import requests

from send_email import send_email

topic = "apple"
api_key = "38833ae41c784deb9d756f26b4635c94"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2023-02-20&" \
      "sortBy=publishedAt&" \
      "apiKey=38833ae41c784deb9d756f26b4635c94&" \
      "language=en"

request = requests.get(url)

content = request.json()

articles = content["articles"]

body = f"Subject: Today's news\n"
for article in articles[:20]:
    if article["title"] is not None:
        body += f"{article['title']}\n" \
                f"{article['description']}\n" \
                f"{article['url']}\n\n"

body = body.encode("utf-8")

send_email(body)
