from app import app
import unittest


class VoteAppTest(unittest.TestCase):

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_404(self):
        tester = app.test_client(self)
        response = tester.get('/nopage', content_type='html/text')
        self.assertEqual(response.status_code, 404)

    def test_socket(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertIn(b'<span id="connected">0</span>', response.data)


if __name__ == '__main__':
    unittest.main()
