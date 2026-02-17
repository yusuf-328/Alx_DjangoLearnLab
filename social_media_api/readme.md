Social Media API
A Django REST Framework API for a social media platform. Supports user registration, login, posts, comments, following, and a dynamic feed.
Endpoints
User Accounts
/api/register/ – Register a new user
/api/login/ – Login and get auth token
/api/profile/ – View/update user profile
/api/follow/<user_id>/ – Follow a user
/api/unfollow/<user_id>/ – Unfollow a user
Posts & Comments
/api/posts/ – List/create posts
/api/posts/<id>/ – Retrieve/update/delete a post
/api/comments/ – List/create comments
/api/comments/<id>/ – Retrieve/update/delete a comment
Feed
/api/feed/ – View posts from followed users
Setup
Copy code
Bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver