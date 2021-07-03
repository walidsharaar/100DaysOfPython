import requests
PIXELA_ENDPOINT="https://pixe.la/v1/users"
TOKEN= "ITcanbeANYSecretKey"
USER="walid"

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
    "id":"graph1",
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

response=requests.post(url=graph_endpoint,json=graph_config,headers=headers)
print(response.text)

