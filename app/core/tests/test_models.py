from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with email."""
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
    
    def test_create_user_with_invalid_email(self):
        """Create user with invalid email."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '1234')

    def test_create_superuser_with_email_successful(self):
        """Test creating a new super user with email."""
        email = 'test@mail.com'
        password = '1234'
        user = get_user_model().objects.create_superuser(
            email=email,
            password=password
        )

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
