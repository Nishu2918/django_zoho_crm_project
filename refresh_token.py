import requests

def refresh_access_token():
    url = "https://accounts.zoho.in/oauth/v2/token"
    params = {
        "refresh_token": "1000.e05cd564289b3296ccd0b6a7511399af.d747b6f9d8c8ebeb5f67933c0e60de5a",
        "client_id": "1000.EB1262RQNXTEV8QWOA1C5AJ8REH1MC",
        "client_secret": "35757a4b0fcfdb34b57eda94f8ec6f64b24361505e",
        "grant_type": "refresh_token"
    }

    response = requests.post(url, params=params)
    data = response.json()
    print("Status Code:", response.status_code)
    print("Response:", data)

    return data.get("access_token")

refresh_access_token()
