import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
API_STOCK = "ZTPJAIZLWVSIOUU9"

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
API_NEWS = "aa442eda099d47d09e2cbb8e1870eaa8"

TWILIO_SID = "AC13b4d703e9bd7502191df26f04a37929"
TWILIO_AUTH_TOKEN = "cc1e0ec60c0ee2aec61101f46b0d0f37"

url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK_NAME}&apikey={API_STOCK}"
r = requests.get(url)
r.raise_for_status()
data = r.json()["Time Series (Daily)"]

# Make a list from dictionary bcs we do not need a keys only value
data_list = [value for (key, value) in data.items()]

yesterday_closing_price = data_list[0]["4. close"]
day_before_yesterday_closing_price = data_list[1]["4. close"]

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "⬆️"
else:
    up_down = "⬇️"
difference_percentage = round((difference / float(yesterday_closing_price)) * 100)

# If TODO4 percentage is greater than 5 then print("Get News").
if abs(difference_percentage) > 1:
    new_params = {
        "apiKey": API_NEWS,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=new_params)
    articles = news_response.json()["articles"]

    three_articles = articles[:3]

    formatted_articles = [(f"{STOCK_NAME}: {up_down}{difference_percentage}%\nHeadlines: {article['title']}. "
                           f"\nBrief: {article['description']}") for article in three_articles]

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_='+12134863846',
            to='+31686288377'
        )
