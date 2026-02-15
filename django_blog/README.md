Django Blog Authentication
Overview
Simple authentication system for a Django blog with:
User registration (with email)
Login & logout
Profile view & email update
Files
forms.py – Custom registration form
views.py – Handles register, login, logout, profile
urls.py – Routes for authentication
templates/blog/ – register.html, login.html, logout.html, profile.html
How to Run
Copy code
Bash
# Activate virtual environment
source venv/Scripts/activate   # Windows

# Apply migrations
python manage.py migrate

# Start server
python manage.py runserver
Visit:
/register/ – Register
/login/ – Log in
/profile/ – View/update profile
/logout/ – Log out
Security
CSRF protection included in all forms
Passwords hashed automatically
Profile page requires login
