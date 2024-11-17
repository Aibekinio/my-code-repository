import unittest
from main import say_hello

class TestHelloFunction(unittest.TestCase):
    def test_say_hello(self):
        self.assertEqual(say_hello("Student"), "Hello, Student!")

if __name__ == '__main__':
    unittest.main()
