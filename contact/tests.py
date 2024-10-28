from django.test import TestCase, Client
from django.urls import reverse
from .models import ContactMessage
from .forms import ContactForm


class ContactMessageModelTest(TestCase):
    def setUp(self):
        self.message = ContactMessage.objects.create(
            name="Test User",
            email="test@example.com",
            phone_number="1234567890",
            message="Test message",
        )

    def test_string_representation(self):
        self.assertEqual(str(self.message), "Test User")

    def test_fields(self):
        self.assertEqual(self.message.name, "Test User")
        self.assertEqual(self.message.email, "test@example.com")
        self.assertEqual(self.message.phone_number, "1234567890")
        self.assertEqual(self.message.message, "Test message")


class ContactFormTest(TestCase):
    def test_valid_form(self):
        data = {
            "name": "Test User",
            "email": "test@example.com",
            "phone_number": "1234567890",
            "message": "Test message",
        }
        form = ContactForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        # Test with invalid email
        data = {
            "name": "Test User",
            "email": "invalid-email",
            "phone_number": "1234567890",
            "message": "Test message",
        }
        form = ContactForm(data=data)
        self.assertFalse(form.is_valid())

    def test_blank_form(self):
        form = ContactForm(data={})
        self.assertFalse(form.is_valid())
        # name, email, and message are required
        self.assertEqual(len(form.errors), 3)


class ViewsTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_view(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")

    def test_about_view(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "about.html")

    def test_events_view(self):
        response = self.client.get(reverse("events"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "events.html")

    def test_join_view(self):
        response = self.client.get(reverse("join"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "join.html")

    def test_contact_view_get(self):
        response = self.client.get(reverse("contact"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "contact/contact.html")
        self.assertIsInstance(response.context["form"], ContactForm)

    def test_contact_view_post_success(self):
        data = {
            "name": "Test User",
            "email": "test@example.com",
            "phone_number": "1234567890",
            "message": "Test message",
        }
        response = self.client.post(reverse("contact"), data)
        self.assertRedirects(response, reverse("success"))
        self.assertEqual(ContactMessage.objects.count(), 1)

    def test_contact_view_post_invalid(self):
        data = {
            "name": "",  # Invalid: empty name
            "email": "test@example.com",
            "phone_number": "1234567890",
            "message": "Test message",
        }
        response = self.client.post(reverse("contact"), data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(ContactMessage.objects.count(), 0)

    def test_success_view(self):
        response = self.client.get(reverse("success"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "contact/success.html")
