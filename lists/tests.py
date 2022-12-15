from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve

from lists.views import home_page

# Create your tests here.


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve("/")
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_corretct_html(self):
        requset = HttpRequest()
        response = home_page(requset)
        html = response.content.decode("utf8")
        self.assertTrue(html.startswith("<html>"))
        self.assertIn("<title>To-Do list</title>", html)
        self.assertTrue(html.endswith("</html>"))
