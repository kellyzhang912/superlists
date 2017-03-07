from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page

# Create your tests here
class HomePageTest(TestCase):
    def test_root_url_resolve_to_home_page_view(self):
        found = resolve('/')
        self.assertEquals(found.func,home_page)
       # self.fail("d")