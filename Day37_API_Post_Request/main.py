import requests
from datetime import datetime
PIXELA_ENDPOINT="https://pixe.la/v1/users"
TOKEN= "ITcanbeANYSecretKey"
USER="walid"
GRAPH_ID="graph1"
today=datetime.now()
DATE=today.strftime("%Y%m%d")

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

pixel_data={
    "date":DATE ,
    "quantity":"6.3"
}
response=requests.post(url=pixel_creation_endpoint,json=pixel_data,headers=headers)
print(response.text)

pixel_update={
    "date":DATE,
    "quantity":"5.1"
}
pixel_update_endpoint=f"{PIXELA_ENDPOINT}/{USER}/graphs/{GRAPH_ID}/{DATE}"

# response = requests.put(url=pixel_update_endpoint,json=pixel_update,headers=headers)
# print(response.text)


pixel_delete_endpoint=f"{PIXELA_ENDPOINT}/{USER}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
response=requests.delete(url=pixel_delete_endpoint,headers=headers)
print(response.text)