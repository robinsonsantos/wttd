# coding: utf-8
from django.contrib.auth import get_user_model
from django.test import TestCase
from eventex.myauth.backends import EmailBackend

class EmailBackendTest(TestCase):
    def setUp(self):
        UserModel = get_user_model()
        UserModel.objects.create_user(username='robinson',
                                      email='robinson@santos.com',
                                      password='abracadabra')
        self.backend = EmailBackend()

    def test_authenticate_with_email(self):
        user = self.backend.authenticate(email='robinson@santos.com',
                                         password='abracadabra')
        self.assertIsNotNone(user)

    def test_wrong_password(self):
        user = self.backend.authenticate(email='robinson@santos.com',
                                         password='wrong')
        self.assertIsNone(user)

    def test_unknown_user(self):
        user = self.backend.authenticate(email='unknown@email.com',
                                         password='abracadabra')
        self.assertIsNone(user)

    def test_get_user(self):
        self.assertIsNotNone(self.backend.get_user(1))

class MultipleEmailsTest(TestCase):
    def setUp(self):
        UserModel = get_user_model()
        UserModel.objects.create_user(username='user1',
                                      email='robinson@santos.com', 
                                      password='abracadabra')
        UserModel.objects.create_user(username='user2',
                                      email='robinson@santos.com', 
                                      password='abracadabra')
        self.backend = EmailBackend()   

    def test_multiple_emails(self):
        user = self.backend.authenticate(email='robinson@santos.com',
                                         password='abracadabra')
        self.assertIsNone(user)

class FunctionalEmailBackendTest(TestCase):
    def setUp(self):
        UserModel = get_user_model()
        UserModel.objects.create_user(username='robinson',
                                      email='robinson@santos.com',
                                      password='abracadabra')

    def test_login_with_email(self):
        result = self.client.login(email='robinson@santos.com',
                                   password='abracadabra')
        self.assertTrue(result)

    def test_login_with_username(self):
        result = self.client.login(username='robinson@santos.com',
                                   password='abracadabra')
        self.assertTrue(result) 
