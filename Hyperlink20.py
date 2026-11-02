
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# URL of the news website
url = "https://news.ycombinator.com"

# Send request to the website
response = requests.get(url)

# Check whether request is successful
if response.status_code == 200:

    # Parse HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all headline links
    headlines = soup.find_all("a")

    print("NEWS HEADLINES AND HYPERLINKS\n")

    for headline in headlines:
        text = headline.get_text(strip=True)
        link = headline.get("href")

        # Check whether headline and link exist
        if text and link:
            full_link = urljoin(url, link)

            print("Headline:", text)
            print("Link:", full_link)
            print("-" * 50)

else:
    print("Failed to access the website")
