# This save 5 headlines from bbc news
import requests
from bs4 import BeautifulSoup

# Gets the url
url = r"https://www.bbc.com/news"
response = requests.get(url)

# Parse html
soup = BeautifulSoup(response.text, "html.parser")

# Save and print
with open("headlines.txt", "w") as f:
    headlines = soup.find_all("h2")[:5]
    try: 
        for i, headline in enumerate(headlines, start=1):
            f.write("--- 5 Headlines of the BBC ---")
            f.write(f"{i}. {headline.get_text(strip=True)}\n")
            print(f"{i}. {headline.get_text(strip=True)}")
            print("Headlines Saved Successfully. ")
    except Exception as e:
        print(f"An unexpected errror occured. {e}")