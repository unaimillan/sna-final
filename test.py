import unittest
from app import app, redis


class WebappTest(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.counter_value = redis.get('counter')

    def tearDown(self):
        redis.set('counter', self.counter_value)

    def test_simple(self):
        self.assertEqual(2 + 2, 4)
        self.assertEqual('hello world', 'hello' + ' ' + 'world')

    def test_response_ok(self):
        resp = self.app.get('/')
        self.assertEqual(resp.status, '200 OK')


if __name__ == '__main__':
    unittest.main()
