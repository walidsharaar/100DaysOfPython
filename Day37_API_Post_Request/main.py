import requests
PIXELA_ENDPOINT="https://pixe.la/v1/users"
user_param ={
    "token":"ITcanbeANYSecretKey",
    "username":"walid",
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

response=requests.post(url=PIXELA_ENDPOINT,json=user_param)
print(response.text)
