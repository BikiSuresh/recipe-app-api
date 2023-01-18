"""
Test for Models
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test Models"""
    def test_create_user_email_successful(self):
        """Test Creating a User with email is Successful"""
        email = 'testa@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test email is normalized for new users."""
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['test2@Example.com', 'test2@example.com'],
            ['TEST3@EXAMPLE.com', 'TEST3@example.com'],
            ['Test4@example.Com', 'Test4@example.com'],
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample123')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raise_error(self):
        """Tes that creating a user without an email raises a ValueError"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'test123')

    def test_create_superuser(self):
        """Test Creating SuperUser"""
        user = get_user_model().objects.create_superuser(
            email='test@example.com',
            password='testsuperuser123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
