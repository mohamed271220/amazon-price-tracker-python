from bs4 import BeautifulSoup
import requests
import pandas as pd
import lxml
import smtplib

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
    ,
    "Accept-Language": "en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7"
    }

response = requests.get('https://www.amazon.com/Acer-SB220Q-Ultra-Thin-Frame-Monitor/dp/B07CVL2D2S/ref=sr_1_5?crid'
                        '=14JVFKWCO26PY',
                        headers=headers)

product_page = response.text

# print(product_page)

soup= BeautifulSoup(product_page,'lxml')

price = soup.select_one('span.a-price-whole').getText()
price=float(price)
print(price)

title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 90

if price < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )
        # or for yahoo
#   try:
#     smtpObj = smtplib.SMTP("smtp.mail.yahoo.com", 587)
#     smtpObj.starttls()
#     smtpObj.login(user=sender, password=password)
#     smtpObj.sendmail(from_addr=sender, to_addrs=receivers, msg=message)
#     print("Successfully sent email")
# except smtplib.SMTPException as e:
#     print(f"Error: unable to send email: {e}")