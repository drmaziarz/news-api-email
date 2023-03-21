import os

import requests

from send_email import send_email, configure

configure()

topic = "apple"

url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2023-02-21&" \
      "sortBy=publishedAt&" \
      f"apikey={os.getenv('api_key')}&" \
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
