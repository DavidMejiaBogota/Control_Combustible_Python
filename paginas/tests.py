from django.test import SimpleTestCase
from django.urls import reverse

class AboutPageTests(SimpleTestCase):

    def setUp(self):
        self.response = self.client.get("/pages/about")

    def test_url_about(self):
        self.assertEqual(self.response.status_code, 200)
    
    def test_html_about(self):
        self.assertTemplateUsed(self.response, "paginas/about.html")
        self.assertContains(self.response, "Aplicación para el control de Combustible")
        self.assertNotContains(self.response, "Curso J. David Mejía / FB/IG DavidDeveloper")
