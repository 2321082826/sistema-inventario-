
import unittest

class TestErrorRelease(unittest.TestCase):

    def test_error_intencional(self):
        self.assertEqual(
            10,
            20,
            "Error intencional para probar RELEASE"
        )

if __name__ == "__main__":
    unittest.main()
