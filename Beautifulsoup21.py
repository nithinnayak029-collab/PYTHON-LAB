
import requests
from bs4 import BeautifulSoup
import csv

# Website URL
url = "https://books.toscrape.com/"

# Send HTTP request
response = requests.get(url)

# Check request status
if response.status_code == 200:

    # Parse HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all products
    products = soup.find_all("article", class_="product_pod")

    # Create CSV file
    with open("products.csv", "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        # Write column headings
        writer.writerow(["Product Name", "Price", "Availability", "Rating"])

        # Extract product information
        for product in products:

            name = product.h3.a["title"]

            price = product.find("p", class_="price_color").text

            availability = product.find(
                "p", class_="instock availability"
            ).text.strip()

            rating = product.find("p", class_="star-rating")["class"][1]

            # Store data in CSV
            writer.writerow([name, price, availability, rating])

    print("Product information successfully saved to products.csv")

else:
    print("Failed to access website")
