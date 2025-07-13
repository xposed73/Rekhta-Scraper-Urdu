import requests
from bs4 import BeautifulSoup
import re

def clean_text(text):
    text = re.sub(r'\s+', ' ', text.strip())
    return text.replace('&nbsp;', ' ')

def is_urdu(text):
    return bool(re.search(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]', text))

def extract_urdu_verses(soup):
    verses = []
    urdu_blocks = soup.select('div[data-roman="off"] .c')

    for container in urdu_blocks:
        for p in container.find_all("p"):
            spans = p.find_all("span")
            words = [clean_text(span.get_text()) for span in spans if clean_text(span.get_text())]
            if not words or not any(is_urdu(word) for word in words):
                continue
            verse = " ".join(words)
            verses.append(verse)

    return verses

def scrape_rekhta_ghazal(url):
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')

        verses = extract_urdu_verses(soup)

        if verses:
            # Save to file only
            with open("ghazal.txt", "w", encoding="utf-8") as f:
                for verse in verses:
                    f.write(verse + "\n")
            print("✅ Ghazal successfully saved to ghazal.txt")
        else:
            print("⚠️ No Urdu verses found on the page.")
    except Exception as e:
        print(f"❌ Error: {e}")

# Rekhta URL
url = "https://www.rekhta.org/ghazals/sitaaron-se-aage-jahaan-aur-bhii-hain-allama-iqbal-ghazals-1?lang=ur"

if __name__ == "__main__":
    scrape_rekhta_ghazal(url)
