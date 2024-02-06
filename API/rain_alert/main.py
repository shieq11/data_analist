import requests
from twilio.rest import Client

api_key = "62074b9622bab32d1e99449cc43a418f"

account_sid = "AC13b4d703e9bd7502191df26f04a37929"
auth_token = "cc1e0ec60c0ee2aec61101f46b0d0f37"

parameters ={
    "lat": 51.723062,
    "lon": 5.138226,
    "appid": api_key,
    "cnt": 4,
}
response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()
print(weather_data)
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella",
        from_='+12134863846',
        to='+31686288377'
    )
    print(message.status)