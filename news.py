import os
import requests

class NewsFeed:
    base_url = 'https://newsapi.org/v2/everything'
    api_key = os.getenv("NEWSAPI_API")
    
    def __init__(self, interest, from_date, to_date, language):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get(self):
        news_url = self._build_url()
        response = requests.get(url=news_url)
        content = response.json()
        email_body = ''
        for article in content['articles']:
            email_body = email_body + f"{article['title']}\n{article['url']}\n\n"
        return email_body

    def _build_url(self):
        news_url = f'{self.base_url}' \
                   f'?qInTitle={self.interest}' \
                   f'&from={self.from_date}' \
                   f'&to={self.to_date}' \
                   f'&language={self.language}' \
                   f'&apiKey={self.api_key}'
        return news_url


if __name__ == "__main__":
    news_feed = NewsFeed(interest='nasa',
                         from_date='2023-03-18',
                         to_date='2023-03-19',
                         language='en')
    print(news_feed.get())
