import yagmail
import pandas as pd
import os
from news import NewsFeed
from datetime import date, datetime, timedelta
import time

df = pd.read_excel("people.xlsx")
user_id = "gammasynchrony2@gmail.com"
user_password = os.getenv("GMAIL_APP_PASSWORD")


def send_email():
    today = (date.today()).strftime("%Y-%m-%d")
    yesterday = (date.today() - timedelta(days=1)).strftime("%Y-%m-%d")
    news_feed = NewsFeed(interest=row['interest'],
                         from_date=yesterday,
                         to_date=today,
                         language="en")
    email = yagmail.SMTP(user=user_id, password=user_password)
    email.send(to=row['email'],
               subject=f"Your {row['interest'].title()} News For Today",
               contents=f"Good morning, {row['name']}!\n"
                        f"See what's new for {row['interest'].title()}!\n"
                        f"{news_feed.get()}")


while True:
    if datetime.now().hour == 8 and datetime.now().minute == 0:
        for index, row in df.iterrows():
            send_email()
    time.sleep(60)

