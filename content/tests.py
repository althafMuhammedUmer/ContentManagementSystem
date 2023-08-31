# content/tests.py

from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Content
from django.core.files.uploadedfile import SimpleUploadedFile

User = get_user_model()

class ContentAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='testuser@gmail.com',first_name='test', last_name='last', phone=1234567890, pincode=123456, password='Testpass123')
        self.client.force_authenticate(user=self.user)

    def test_create_content(self):
        data = {
            "title": "Test Title",
            "body": "Test Body",
            "summary": "Test Summary",
            "document": SimpleUploadedFile("test.pdf", b"file_content", content_type="application/pdf"),
            "categories": "Category1,Category2"
        }

        response = self.client.post('/api/create', data, format="multipart")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_get_content_list(self):
        response = self.client.get('/api/content/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_content_by_id(self):
        content = Content.objects.create(title='Test Title', body='Test Body', author=self.user)
        response = self.client.get(f'/api/content/{content.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_content(self):
        content = Content.objects.create(title='Test Title', body='Test Body', author=self.user)
        data = {
            "title": "Updated Title",
            "body": "Updated Body",
            "summary": "Updated Summary",
            "document": SimpleUploadedFile("updated.pdf", b"file_content", content_type="application/pdf"),
            "categories": "Category3,Category4"
        }

        response = self.client.put(f'/api/content_action/{content.id}/', data,  format="multipart")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        content.refresh_from_db()
        self.assertEqual(content.title, "Updated Title")
        self.assertEqual(content.categories.count(), 2)  # Check updated categories count


    def test_delete_content(self):
        content = Content.objects.create(title='Test Title', body='Test Body', author=self.user)
        response = self.client.delete(f'/api/content_action/{content.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Content.objects.filter(title='Test Title').exists())
