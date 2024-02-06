import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth
import os

APP_ID = os.environ["ENV_APP_ID"]
API_KEY = os.environ["ENV_API_KEY"]
GENDER = "male"
WEIGHT_KG = 80
HEIGHT_CM = 175
AGE = 33
basic = HTTPBasicAuth(os.environ["BASIC_NAME"], os.environ["BASIC_PASSWORD"])

NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
response = requests.post(url=NUTRITIONIX_ENDPOINT, json=parameters, headers=headers)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

sheet_endpoint = os.environ["SHEET_ENDPOINT"]

for exercise in result["exercises"]:
    sheet_inputs = {
        "arkusz1": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, auth=basic)
print(sheet_response.text)