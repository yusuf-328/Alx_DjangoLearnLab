from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import Book


class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create users
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword"
        )

        self.admin_user = User.objects.create_superuser(
            username="admin",
            password="adminpassword",
            email="admin@test.com"
        )

        # Create sample book
        self.book = Book.objects.create(
            title="Test Book",
            author="Test Author",
            publication_year=2024
        )

        self.book_list_url = reverse("book-list")
        self.book_detail_url = reverse("book-detail", args=[self.book.id])

    # -----------------------
    # READ (List & Detail)
    # -----------------------
    def test_get_books_list(self):
        response = self.client.get(self.book_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)

    def test_get_single_book(self):
        response = self.client.get(self.book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.book.title)

    # -----------------------
    # CREATE
    # -----------------------
    def test_create_book_authenticated(self):
        self.client.login(username="admin", password="adminpassword")

        data = {
            "title": "New Book",
            "author": "New Author",
            "publication_year": 2023
        }

        response = self.client.post(self.book_list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_create_book_unauthenticated(self):
        data = {
            "title": "Unauthorized Book",
            "author": "Unknown",
            "publication_year": 2022
        }

        response = self.client.post(self.book_list_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # -----------------------
    # UPDATE
    # -----------------------
    def test_update_book_authenticated(self):
        self.client.login(username="admin", password="adminpassword")

        data = {
            "title": "Updated Title",
            "author": "Updated Author",
            "publication_year": 2025
        }

        response = self.client.put(self.book_detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Title")

    def test_update_book_unauthenticated(self):
        data = {
            "title": "Hack Update"
        }

        response = self.client.put(self.book_detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # -----------------------
    # DELETE
    # -----------------------
    def test_delete_book_authenticated(self):
        self.client.login(username="admin", password="adminpassword")

        response = self.client.delete(self.book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_delete_book_unauthenticated(self):
        response = self.client.delete(self.book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # -----------------------
    # FILTERING / SEARCH / ORDERING
    # -----------------------
    def test_filter_books_by_title(self):
        response = self.client.get(self.book_list_url, {"title": "Test Book"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_order_books_by_publication_year(self):
        response = self.client.get(self.book_list_url, {"ordering": "publication_year"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)