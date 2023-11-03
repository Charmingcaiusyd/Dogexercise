from django.test import TestCase
from .models import User, Pet
from django.contrib.auth.hashers import check_password
from django.core.files.uploadedfile import SimpleUploadedFile
class UserTestCase(TestCase):

    def setUp(self):
        # 创建用户
        self.user = User.objects.create(
            username='testuser',
            email='testuser@example.com',
            password='password123',
            age=25
        )

    def test_user_creation(self):
        # 测试用户创建
        self.assertEqual(self.user.username, 'testuser')
        self.assertTrue(check_password('password123', self.user.password))
        self.assertEqual(self.user.email, 'testuser@example.com')
        self.assertEqual(self.user.age, 25)

    def test_user_methods(self):
        # 测试 User 模型中的方法
        user_info = self.user.get_user_info()
        self.assertEqual(user_info['username'], 'testuser')
        self.assertEqual(user_info['email'], 'testuser@example.com')

class PetTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create( 
            username='testuser',
            email='testuser@example.com',
            password='password123',
            age=25 )
        with open('/Users/xuzhenke/Desktop/Group-15/pets/test_image/test_image.jpg', 'rb') as img:
            photo = SimpleUploadedFile(name='test_image.jpg', content=img.read(), content_type='image/jpg')
        self.pet = Pet.objects.create(owner=self.user, 
                                      name='Buddy',
                                      breed = 'test',
                                      weight=10,
                                      hair='long',
                                      food_preference='meat',
                                      temperament='warm',
                                      photo=photo

                                      )

    def test_pet_creation(self):
        self.assertEqual(self.pet.name, 'Buddy')
        self.assertEqual(self.pet.owner, self.user)

    def test_pet_methods(self):
        pet_info = self.pet.get_pet_info()
        self.assertEqual(pet_info['name'], 'Buddy')
        self.assertEqual(pet_info['owner']['username'], 'testuser')