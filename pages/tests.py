from django.test import TestCase, SimpleTestCase
from django.urls import reverse

# Create your tests here.
class HomepageTests(SimpleTestCase):
    #smoke test to confirm if the page is working or not
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code,200)
    
    #smoke test to confirm if the page is working or not using the name of the url    
    def test_url_available_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code,200)
    
    #test to confirm if the correct template is being used    
    def test_template_name_correct(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response,"home.html")
    
    #test to confirm if the correct content is being displayed in the template
    def test_template_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response,"HomePageHere")
        

class AboutpageTests(SimpleTestCase):
    #smoke test to confirm if the page is working or not
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code,200)

    #smoke test to confirm if the page is working or not using the name of the url
    def test_url_available_by_name(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code,200)
    
    #test to confirm if the correct template is being used
    def test_template_name_correct(self):
        response = self.client.get(reverse("about"))
        self.assertContains(response,"about.html")

    #test to confirm if the correct content is being displayed in the template
    def test_template_content(self):
        response = self.client.get(reverse("about"))
        self.assertContains(response,"AboutPage")