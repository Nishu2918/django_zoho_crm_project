import requests

# Replace with your actual values
client_id = "1000.BO2K3ZRJLGTRXN89UGDKYQ47GJKPSF"
client_secret = "3d91a0c1a5b30990bfa7d540e1fdbb4733dd9c73b6"
redirect_uri = "http://localhost"
code = "1000.2b7808c5c54ba8e241239322aa7ba1c2.3a57dbfa67810831122c73e444ba6e1d"  # Replace this with freshly generated code!

# Token request URL
url = "https://accounts.zoho.in/oauth/v2/token"

# Data to be sent in the POST request
data = {
    "grant_type": "authorization_code",
    "client_id": client_id,
    "client_secret": client_secret,
    "redirect_uri": redirect_uri,
    "code": code
}

# Make the request
response = requests.post(url, data=data)

# Print the response
print("Status Code:", response.status_code)
print("Response:", response.json())
