from django.test import TestCase, Client
from .models import User,Seller
from django.urls import reverse

class SellerRegisterTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('seller_register')  

    def test_register_success(self):
        response = self.client.post(self.register_url, {
            'username': 'new_user',
            'password': 'password123',
            'confirm_password': 'password123',
            'email': 'new_user@example.com',
            'age': '25'
        })
        self.assertEqual(response.status_code, 302)  # 期望重定向到登录页面
        self.assertTrue(Seller.objects.filter(username='new_user').exists())

    def test_register_with_missing_fields(self):
        response = self.client.post(self.register_url, {
            'username': 'new_user',
            'password': 'password123',
            'confirm_password': 'password123',
            # 'email': 'new_user@example.com',
            'age': '25'
        })
        self.assertEqual(response.status_code, 302)  # 期望重定向到注册页面
        self.assertFalse(Seller.objects.filter(username='new_user').exists())
