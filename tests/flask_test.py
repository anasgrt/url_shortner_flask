import unittest
import string
from src.app import app, generate_short_url, shortened_urls

class TestShortURLApp(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        
    def test_generate_short_url(self):
        length = 6
        short_url = generate_short_url(length)
        self.assertEqual(len(short_url), length)

        allowed_chars = set(string.ascii_letters + string.digits + '_')
        self.assertTrue(all(char in allowed_chars for char in short_url))

    def test_index_route(self):
        response = self.app.get('/shorten')
        self.assertEqual(response.status_code, 200)

    def test_shorten_url(self):
        response = self.app.post('/shorten', json=dict(url='https://www.example.com'))
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'Shortened URL', response.data) # check if this is json and contains the shortened code

    def test_shorten_url_with_shortcode(self):
        response = self.app.post('/shorten', json=dict(url='https://www.example.com', shortcode='123456'))
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'Shortened URL', response.data) # check if shortcode is used

    def test_shorten_url_with_existing_shortcode(self):
        shortcode = generate_short_url()
        shortened_urls[shortcode] = 'https://www.example.com'
        response = self.app.post('/shorten', json=dict(url='https://www.example.com', shortcode=shortcode))
        self.assertEqual(response.status_code, 409)
        self.assertIn(f'Shortcode {shortcode} already exists'.encode(), response.data)
    

    def test_shorten_url_with_invalid_shortcode(self):
        shortcode = 'invalid_shortcode'
        response = self.app.post('/shorten', json={'url': 'https://www.example.com', 'shortcode': shortcode})
        self.assertEqual(response.status_code, 412)
        self.assertIn(b'Invalid shortcode', response.data)

    def test_redirect_to_url(self):
        shortcode = generate_short_url()
        shortened_urls[shortcode] = 'https://www.example.com'
        response = self.app.get('ewx123')
        self.assertEqual(response.status_code, 302)
        self.assertIn(b'https://www.example.com', response.data)

    def test_invalid_shortcode_redirect(self):
        response = self.app.get('/invalid_shortcode')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'No URL found', response.data)

if __name__ == '__main__':
    unittest.main()
