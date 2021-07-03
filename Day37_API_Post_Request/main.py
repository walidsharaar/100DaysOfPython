import requests
PIXELA_ENDPOINT="https://pixe.la/v1/users -d "
user_param ={
    "token":"ITcanbeANYSecretKey",
    "username":"Walid",
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

requests.post(url=PIXELA_ENDPOINT,json=user_param)
