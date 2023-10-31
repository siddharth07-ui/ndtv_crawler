import requests
import csv
import io
import logging
import logging.handlers
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)

URL = "https://www.ndtv.com/"

def scrape_news():
    """
    Scrape news articles from NDTV website and save them to a CSV file.
    """
    # Create a session object
    session = requests.Session()

    # Make a GET request to the website using the session object
    response = session.get(URL, timeout=10)

    # Create a BeautifulSoup object
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all the news articles on the page
    articles = soup.find_all("a", class_="item-title")

    # Create a buffered CSV writer object
    buffer = io.StringIO()
    writer = csv.writer(buffer)
    writer.writerow(["News_Title", "News_Link"])  # Write the header row

    # Iterate over each article and extract the title and link
    for article in articles:
        # Check if article.text has length less than 20. Text with length less than 20 are advertisements
        if len(article.text) < 20:
            pass
        else:
            title = article.text.replace(":", "").replace("-", ",").replace(" , ", ", ")
            title = title.strip()
            link = article.get("href")
            writer.writerow([title, link])  # Write the data row

    # Write the contents of the buffer to the file
    with open("news.csv", "w", newline="", encoding="utf-8") as csvfile:
        logger.info('Created CSV file containing news articles.')
        csvfile.write(buffer.getvalue())

if __name__ == '__main__':
    logger.info(f"Running scraper for NDTV website at {URL}")
    scrape_news()