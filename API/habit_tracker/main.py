import requests
from datetime import datetime

USERNAME = "shieq"
TOKEN = "sw2defrsg2fwrgwrgw"
GRAPH_ID = "graph1"
your_graph = "https://pixe.la/v1/users/shieq/graphs/graph1.html"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "New graph",
    "unit": "h",
    "type": "float",
    "color": "kuro",
 }
headers = {
    "X-USER-TOKEN": TOKEN,
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("Ile godzin dziś się uczyłeś? "),
}

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)

# Zmiana wartości "pixela"
# update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
#
# new_pixel_data = {
#     "quantity": "0.5"
# }
# change_pixela = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(change_pixela.text)

# Usuwanie jednego z pixeli

# delete_pixela = requests.delete(url=update_endpoint, headers=headers)
# print(delete_pixela.text)
