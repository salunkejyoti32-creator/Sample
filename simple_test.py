import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'attendance_project.settings')
django.setup()

from django.contrib.auth.hashers import make_password, check_password

# Test password hashing directly
password = "password123"
hashed = make_password(password)
print(f"Original: {password}")
print(f"Hashed: {hashed}")
print(f"Check result: {check_password(password, hashed)}")

# Test with wrong password
print(f"Wrong password check: {check_password('wrongpass', hashed)}")