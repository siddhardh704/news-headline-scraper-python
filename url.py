import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

# Find headlines
headlines = soup.find_all("h2")

with open(r"C:\Users\siddh\OneDrive\Desktop\siddhardh\headlines.txt", "w", encoding="utf-8") as file:
    for i, headline in enumerate(headlines, start=1):
        text = headline.get_text(strip=True)
        if text:
            file.write(f"{i}. {text}\n")
print("Headlines saved to headlines.txt")