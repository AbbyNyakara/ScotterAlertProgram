# Import the modules
import requests
from bs4 import BeautifulSoup
import smtplib

USERNAME = "yourEmail@email.com"
PASSWORD = "password"
ITEM_LINK = "https://www.amazon.com/Folding-Kick-Scooter-Adults-Kids/dp/B08SSSRNHT/ref=sr_1_2_sspa?dchild=1&keywords=electric+scooter+for+adults&qid=1633575045&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUE2RlRMWThHV1FZVjYmZW5jcnlwdGVkSWQ9QTA5NTU1NjUyUVBWUDdYOVY4WDlHJmVuY3J5cHRlZEFkSWQ9QTAxMTY3NDgxTkNXTlYxVDRSOVpPJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="

headers = {
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
response = requests.get(url="https://www.amazon.com/Folding-Kick-Scooter-Adults-Kids/dp/B08SSSRNHT/ref=sr_1_2_sspa?dchild=1&keywords=electric+scooter+for+adults&qid=1633575045&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUE2RlRMWThHV1FZVjYmZW5jcnlwdGVkSWQ9QTA5NTU1NjUyUVBWUDdYOVY4WDlHJmVuY3J5cHRlZEFkSWQ9QTAxMTY3NDgxTkNXTlYxVDRSOVpPJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==",
                        headers=headers)
amazon_data = response.text

# Use Beautiful soup to scrape the Website
soup = BeautifulSoup(amazon_data, "html.parser")

# Get the Price of the item
price = soup.find(id="priceblock_ourprice")
print(price)
item_amount = float(price.strip("$"))
print(item_amount)

# Use the smtplib library to send yourself an email when the item goes below a certain amount
threshold_amount = 50

if item_amount <= threshold_amount:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=USERNAME, password=PASSWORD)
        message = f"Hello there Abby the price is now at {item_amount}. You can now buy the product from {ITEM_LINK}!"
        connection.sendmail(from_addr=USERNAME,
                            to_addrs="yourEmail@email.com",
                            msg=f"Subject: AMAZON PRICE ALERT! \n\n {message}")
