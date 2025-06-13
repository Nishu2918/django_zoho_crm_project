import os
import requests
from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN = os.getenv("ZOHO_ACCESS_TOKEN")
REFRESH_TOKEN = os.getenv("ZOHO_REFRESH_TOKEN")
CLIENT_ID = os.getenv("ZOHO_CLIENT_ID")
CLIENT_SECRET = os.getenv("ZOHO_CLIENT_SECRET")

def refresh_access_token():
    url = "https://accounts.zoho.in/oauth/v2/token"
    params = {
        "refresh_token": REFRESH_TOKEN,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": "refresh_token"
    }
    response = requests.post(url, params=params)
    data = response.json()

    if "access_token" in data:
        print("✅ Access token refreshed.")
        return data["access_token"]
    else:
        print("❌ Failed to refresh access token:", data)
        return None

def get_zoho_leads():
    global ACCESS_TOKEN

    url = "https://www.zohoapis.in/crm/v2/Leads"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }

    response = requests.get(url, headers=headers)
    
    if response.status_code == 401:
        print("⚠️ Token expired. Refreshing...")
        ACCESS_TOKEN = refresh_access_token()
        headers["Authorization"] = f"Bearer {ACCESS_TOKEN}"
        response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print("❌ Error fetching leads:", response.status_code, response.text)
        return {"error": "Failed to fetch leads", "details": response.text}
