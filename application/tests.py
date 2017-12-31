from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Category, Items
import json


class GetByIdItemTests(APITestCase):
    def test_create_account(self):
        url = 'http://127.0.0.1:8000/application/api/detail-item/1/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Items.objects.get(pk=1).title, response.GET['title'])

class GetCategoriesTests(APITestCase):
    def test_create_account(self):
        url = 'http://127.0.0.1:8000/application/api/categories/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json.dumps(Category.objects.all()), response.GET)

class GetItemsTests(APITestCase):
    def test_create_account(self):
        url = 'http://127.0.0.1:8000/application/api/iitems/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json.dumps(Items.objects.all()), response.GET)