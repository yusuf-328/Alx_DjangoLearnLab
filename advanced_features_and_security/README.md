# 📚 Django Permissions & Groups Setup (LibraryProject)

This project demonstrates **how to implement and manage custom permissions and groups in Django** to restrict access to different parts of the application.

---

## ✅ 1. Custom Permissions (bookshelf/models.py)

In `Book` model, custom permissions are defined inside the `Meta` class:

```python
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)

    class Meta:
        permissions = [
            ("can_view", "Can view book"),
            ("can_create", "Can create book"),
            ("can_edit", "Can edit book"),
            ("can_delete", "Can delete book"),
        ]
✅ 2. Groups & Permissions (Django Admin)
Groups created:
Group Name
Permissions Assigned
Viewers
can_view
Editors
can_view, can_create, can_edit
Admins
can_view, can_create, can_edit, can_delete
These groups are created manually through the Django Admin interface.
✅ 3. Permission Checks in Views (bookshelf/views.py)
Views are protected using the permission_required decorator:
Copy code
Python
@permission_required('bookshelf.can_view', raise_exception=True)
def list_books(request):
    ...
This ensures only users with the right permissions can access the pages.
✅ 4. How to Test
Go to Django Admin
Create users (e.g., viewer_user, editor_user, admin_user)
Assign each user to a group
Login with each user and test access:
Viewer can only see books
Editor can add & edit books
Admin can delete books
Notes
Permissions are created after migrations
Always run:
Copy code
Bash
python manage.py makemigrations
python manage.py migrate