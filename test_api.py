import requests
import json

# Test login API
url = "http://localhost:8000/user/login-user/"
data = {
    "username": "testuser",
    "password": "password123"
}

try:
    response = requests.post(url, json=data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
except Exception as e:
    print(f"Error: {e}")