import requests
from datetime import datetime
PIXELA_ENDPOINT="https://pixe.la/v1/users"
TOKEN= "ITcanbeANYSecretKey"
USER="walid"
GRAPH_ID="graph1"

user_param ={
    "token":TOKEN,
    "username":USER,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

# response=requests.post(url=PIXELA_ENDPOINT,json=user_param)
# print(response.text)

graph_endpoint=f"{PIXELA_ENDPOINT}/{USER}/graphs"
graph_config={
    "id":GRAPH_ID,
    "name":"Running",
    "unit":"km",
    "type":"float",
    "color":"ajisai",
}

# graph_response=requests.post(url=graph_endpoint,json=graph_config)
# print(graph_response.text)

headers={
    "X-USER-TOKEN":TOKEN
}

# response=requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)

pixel_creation_endpoint =f"{PIXELA_ENDPOINT}/{USER}/graphs/{GRAPH_ID}"
today=datetime.now()
pixel_data={
    "date": today.strftime("%Y%m%d"),
    "quantity":"6.3"
}
response=requests.post(url=pixel_creation_endpoint,json=pixel_data,headers=headers)
print(response.text)
