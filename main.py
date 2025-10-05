# main.py
import time
import requests
from bs4 import BeautifulSoup
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, CHECK_INTERVAL

APPLE_URL = "https://www.apple.com/my/shop/buy-iphone/iphone-17-pro/6.9-inch-display-256gb-silver"

def send_telegram_message(message):
    """Send a Telegram message using your bot."""
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    requests.post(url, data=payload)

def check_stock():
    """Check if iPhone 17 Pro Max is in stock."""
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(APPLE_URL, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        if "Currently unavailable" in soup.text or "Out of stock" in soup.text:
            print("❌ Still unavailable")
            return False
        else:
            print("✅ iPhone might be available!")
            return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def main():
    while True:
        print("Checking iPhone 17 Pro Max stock...")
        in_stock = check_stock()
        if in_stock:
            send_telegram_message("📱 iPhone 17 Pro Max may be IN STOCK at The Exchange TRX! Go check Apple Store now!")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
