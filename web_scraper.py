"""
Task 3: Scrape the title and metadata of a webpage and save it to a file.
Concepts: requests, re, file handling
"""
import re
import os
import requests
from datetime import datetime

def scrape_webpage(url, output_file):
    result = {"url": url, "title": "", "description": "", "status": 0, "headings": []}
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
    }
    print(f"  Fetching: {url}")
    response = requests.get(url, headers=headers, timeout=10)
    result["status"] = response.status_code
    if response.status_code != 200:
        print(f"  Warning: Server returned status {response.status_code}")

    html = response.text
    title_match = re.search(r'<title[^>]*>(.*?)</title>', html, re.IGNORECASE | re.DOTALL)
    result["title"] = re.sub(r'\s+', ' ', title_match.group(1)).strip() if title_match else "No title found"
    desc_match = re.search(r'<meta[^>]+name=["\']description["\'][^>]+content=["\'](.*?)["\']', html, re.IGNORECASE)
    result["description"] = desc_match.group(1).strip() if desc_match else "No description found"
    h1_tags = re.findall(r'<h1[^>]*>(.*?)</h1>', html, re.IGNORECASE | re.DOTALL)
    result["headings"] = [re.sub(r'<[^>]+>', '', h).strip() for h in h1_tags[:5]]

    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("=" * 60 + "\n")
        f.write("  WEB SCRAPE RESULT\n")
        f.write("=" * 60 + "\n")
        f.write(f"  URL         : {url}\n")
        f.write(f"  Status Code : {result['status']}\n")
        f.write(f"  Scraped At  : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"TITLE:\n  {result['title']}\n\n")
        f.write(f"DESCRIPTION:\n  {result['description']}\n\n")
        if result.get("headings"):
            f.write("H1 HEADINGS:\n")
            for h in result["headings"]:
                if h:
                    f.write(f"  - {h}\n")
    print(f"  Status   : {result['status']}")
    print(f"  Title    : {result['title']}")
    print(f"  Saved to : {output_file}")
    return result

if __name__ == "__main__":
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    out  = os.path.join(base, "output", "scraped_title.txt")
    print("=" * 60)
    print("  WEB PAGE SCRAPER")
    print("=" * 60)
    # Using Wikipedia - always accessible for scraping
    result = scrape_webpage("https://en.wikipedia.org/wiki/Python_(programming_language)", out)

# NOTE: In restricted network environments, this script may not reach external URLs.
# Run it on your local machine to fetch live web data.
