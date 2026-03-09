from django.test import TestCase
from django.urls import reverse
from .models import Member

class RegisterMemberTest(TestCase):
    def test_member_registration(self):
        # Data for registration
        data = {
            'first_name': 'John',
            'second_name': 'Doe',
            'phone_number': '0712345678',
            'year_of_study': 1,
            'class_name': 'Bible Scholars'
        }
        
        # Post the data to the registration view
        response = self.client.post(reverse('register_member'), data)
        
        # Check if the registration was successful (redirects back to the same page or redirects depending on implementation)
        # In our implementation, we redirect to 'register_member'
        self.assertEqual(response.status_code, 302)
        
        # Check if member was saved to database
        self.assertTrue(Member.objects.filter(first_name='John', second_name='Doe').exists())
        
    def test_registration_view(self):
        # Test if the view loads properly
        response = self.client.get(reverse('register_member'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register/register.html')

