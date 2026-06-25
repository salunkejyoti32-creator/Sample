import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'attendance_project.settings')
django.setup()

from attendance.models import User
from django.contrib.auth.hashers import check_password

# Test login logic
username = "testuser"
password = input("Enter password for 'test' user: ")

try:
    user = User.objects.get(username=username)
    print(f"User found: {user.username}")
    print(f"Stored password hash: {user.password[:50]}...")
    
    if check_password(password, user.password):
        print("SUCCESS: Password matches!")
    else:
        print("ERROR: Password does not match")
        
except User.DoesNotExist:
    print("ERROR: User not found")