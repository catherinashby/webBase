from django.urls import resolve
from django.http import HttpRequest
from django.test import TestCase

from webBase.views import frontpage

class HomePageTest( TestCase ):

    def test_root_url_resolves_to_front_page_view( self ):
        found = resolve( '/' )
        self.assertEqual( found.func, frontpage )

    def test_front_page_returns_correct_html(self):
        request = HttpRequest()
        response = frontpage( request )
        self.assertTrue( response.content.startswith( b'\n<!DOCTYPE html>' ) )
        self.assertIn( b'<title>web Base</title>', response.content )
        self.assertTrue( response.content.endswith( b'</html>' ) )