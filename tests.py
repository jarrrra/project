import unittest
import main

class Test(unittest.TestCase):
    def test_main(self):
        self.assertNoLogs(main.main())

    def test_hello(self):
        self.assertEqual(type(main.hello()), str)

if __name__ == "__main__":
    unittest.main()