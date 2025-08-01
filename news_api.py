import requests
from datetime import datetime, timedelta

query = input("What type of news are you interested in today? ")
api = "a0ebe079dc1e4c5997614a09ca1560ea"

# Use past 7 days as the date range
from_date = (datetime.today() - timedelta(days=7)).strftime('%Y-%m-%d')

url = f"https://newsapi.org/v2/everything?q={query}&from={from_date}&sortBy=publishedAt&apiKey={api}"

print("\nFetching from URL:", url)
response = requests.get(url)
data = response.json()

# Check if the API returned an error
if data.get("status") != "ok":
    print("Error:", data.get("message", "Something went wrong"))
else:
    articles = data.get("articles", [])
    if not articles:
        print("No articles found for your query.")
    else:
        print(f"\nTop {len(articles)} articles for '{query}':\n")
        for index, article in enumerate(articles[:30]):  # limit to first 30
            print(f"{index + 1}. {article.get('title')}")
            print(f"   🔗 {article.get('url')}\n" + "*" * 40 + "\n")


