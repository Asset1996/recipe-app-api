from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
import pprint

class TestAdmin(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            email='test@mail.com',
            password='1234',
            name='Test full name'
        )
        self.admin_user = get_user_model().objects.create_superuser(
            email='test_admin@mail.com',
            password='123456'
        )
        self.client.force_login(self.admin_user)

    def test_users_listed(self):
        """Test that users listed in our page."""
        url = reverse('admin:core_user_changelist')
        response = self.client.get(url)
        self.assertContains(response, self.user.email)
        self.assertContains(response, self.user.name)

    def test_users_change_page(self):
        """Test the users information update page."""
        url = reverse('admin:core_user_change', args=[self.user.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_users_add_page(self):
        """Test the users information add page."""
        url = reverse('admin:core_user_add')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

