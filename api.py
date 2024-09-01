import requests
import json


# OAuth2 token endpoint
url = "https://api.chenosis.io/oauth/client/accesstoken?grant_type=client_credentials"

# Client credentials (obtained from the API provider)
client_id = 'i5leGGpAiGLALOc1quSGJkf8JSG7Di0d'
client_secret = '1PwOBPcNd8Wt0Mq9'

# Headers and payload
headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}
payload = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret
}

# Making the POST request
response = requests.post(url, headers=headers, data=payload)

# Checking the response
if response.status_code == 200:
    # Successful request
    token_data = response.json()
    access_token = token_data['access_token']
    print("Access Token:", access_token)
else:
    # Something went wrong
    print("Failed to obtain token")
    print("Status Code:", response.status_code)
    print("Response:", response.text)


url = "https://api.chenosis.io/aizatron/facial-recognition/add"

# Proper JSON formatting using a Python dictionary then converting it to a JSON formatted string
payload_dict = {
    "name": "lesedi",
    "image": "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"
}
# payload = json.dumps(payload_dict)  # Converting dictionary to JSON formatted string

# headers = {
    
#     'Authorization': f'Bearer {23pX76P0PlPlbeuIasZf5d0bEn4o}',
    
#     'Content-Type': 'application/json'  # Ensuring the content type is set to application/json
# }


# response = requests.post(url, headers=headers, data=payload)  # Using post directly for clarity

print(response.text)

def use_access_token(access_token):
    url = "https://api.chenosis.io/aizatron/facial-recognition/add"
    headers = {
    
    'Authorization': f'Bearer {access_token}'
    }
    response = requests.post(url, headers=headers, data=payload)  # Using post directly for clarity
    return response.json()