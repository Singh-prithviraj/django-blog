from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status

from .models import Author, Post


class BlogAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword123"
        )

        self.author = Author.objects.create(
            user=self.user
        )

    def test_health(self):
        response = self.client.get("/api/health/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["status"], "ok")

    def test_readiness(self):
        response = self.client.get("/api/readiness/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["status"], "ready")

    def test_get_posts(self):
        response = self.client.get("/api/posts/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_post_requires_authentication(self):
        data = {
            "title": "Test Post",
            "content": "Test content"
        }

        response = self.client.post("/api/posts/", data)

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED
        )

    def test_create_post(self):
        self.client.force_authenticate(user=self.user)

        data = {
            "title": "My Test Post",
            "content": "This is test content."
        }

        response = self.client.post("/api/posts/", data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "My Test Post")