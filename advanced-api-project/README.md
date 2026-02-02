
Advanced API Project

Overview
This Django REST Framework project demonstrates custom views and generic views to manage a Book model. It implements full CRUD functionality with proper permission settings.
List all books – public access
Retrieve a single book – public access
Create, update, delete books – restricted to authenticated users
The project focuses on using DRF generic views for simplicity, modularity, and proper API behavior.
Project Structure
Copy code

advanced-api-project/
├─ api/
│  ├─ models.py        # Author and Book models
│  ├─ serializers.py   # Custom serializers with validation
│  ├─ views.py         # Generic views for CRUD operations
│  └─ urls.py          # URL patterns connecting views
├─ advanced-api-project/
│  └─ settings.py      # Django project settings
└─ manage.py           # Django management commands
Models
Book
title (string) – book title
publication_year (integer) – year of publication
author (foreign key) – links to Author
Author
name (string) – author name
books – nested relation to Book
Serializers
BookSerializer – serializes all Book fields, validates publication_year
AuthorSerializer – includes name and nested BookSerializer to list related books
Views & Endpoints
List all books
View: BookListView
Method: GET
URL: /books/
Permission: Public (AllowAny)
Retrieve a single book
View: BookDetailView
Method: GET
URL: /books/<id>/
Permission: Public (AllowAny)
Create a book
View: BookCreateView
Method: POST
URL: /books/create/
Permission: Authenticated users only
Update a book
View: BookUpdateView
Method: PUT
URL: /books/<id>/update/
Permission: Authenticated users only
Delete a book
View: BookDeleteView
Method: DELETE
URL: /books/<id>/delete/
Permission: Authenticated users only
Permissions
View
Permission
ListView
AllowAny
DetailView
AllowAny
CreateView
IsAuthenticated
UpdateView
IsAuthenticated
DeleteView
IsAuthenticated
Testing
Use Postman or curl to test endpoints:
GET /books/ – returns all books
GET /books/1/ – returns book with ID 1
POST /books/create/ – create a book (requires auth)
PUT /books/1/update/ – update book with ID 1 (requires auth)
DELETE /books/1/delete/ – delete book with ID 1 (requires auth)
Notes
Generic views (ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView) simplify CRUD operations and automatically handle request/response formatting.
Permissions are applied at view level to control access.
Validation for publication_year ensures no future-dated books are added.
