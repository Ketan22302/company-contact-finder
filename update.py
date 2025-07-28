import schedule
import time
from scraper import EnhancedScraper

def daily_update():
    scraper = EnhancedScraper()
    # Add your update logic here

schedule.every().day.at("00:00").do(daily_update)

while True:
    schedule.run_pending()
    time.sleep(1)
