from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with email confirmation"""
        email = 'test@mail.com'
        password = '1234'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    
    def test_create_user_with_normalized_email(self):
        """Create user with normalized email."""
        email = 'test@EXAMPLE.COM'
        password = '1234'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )
        self.assertEqual(user.email, email.lower())