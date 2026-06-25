#!/usr/bin/env python
"""
Test script to verify login functionality
"""

import os
import django
import requests
import json

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'attendance_project.settings')
django.setup()

from attendance.models import User

def test_login():
    """Test login with existing users"""
    users = User.objects.all()
    
    print("Available users in database:")
    for user in users:
        print(f"- Username: {user.username}, Email: {user.email}")
    
    if users.exists():
        # Test with first user
        test_user = users.first()
        print(f"\nTesting login for user: {test_user.username}")
        
        # You can test this with your actual password
        # Replace 'your_password' with the actual password for this user
        test_password = input(f"Enter password for {test_user.username}: ")
        
        # Test the login endpoint (assuming your server is running on localhost:8000)
        login_data = {
            "username": test_user.username,
            "password": test_password
        }
        
        try:
            response = requests.post('http://localhost:8000/user/login-user/', 
                                   json=login_data,
                                   headers={'Content-Type': 'application/json'})
            
            print(f"Response Status: {response.status_code}")
            print(f"Response Body: {response.json()}")
            
        except requests.exceptions.ConnectionError:
            print("Server not running. Start your Django server with: python manage.py runserver")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    test_login()