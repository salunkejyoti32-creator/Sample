#!/usr/bin/env python
"""
Script to hash existing plain text passwords in the database.
Run this once after updating your authentication system.
"""

import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'attendance_project.settings')
django.setup()

from django.contrib.auth.hashers import make_password
from attendance.models import User

def hash_existing_passwords():
    """Hash all existing plain text passwords"""
    users = User.objects.all()
    updated_count = 0
    
    for user in users:
        # Check if password is already hashed (Django hashed passwords start with algorithm identifier)
        if not user.password.startswith(('pbkdf2_', 'bcrypt', 'argon2')):
            print(f"Hashing password for user: {user.username}")
            user.password = make_password(user.password)
            user.save()
            updated_count += 1
        else:
            print(f"Password already hashed for user: {user.username}")
    
    print(f"\nCompleted! Updated {updated_count} user passwords.")

if __name__ == "__main__":
    hash_existing_passwords()