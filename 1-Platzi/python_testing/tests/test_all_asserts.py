import unittest

class AllAssertsTest(unittest.TestCase):
    def test_all_asserts(self):
        self.assertTrue(True)
        self.assertFalse(False)
        self.assertEqual(1, 1)
        self.assertNotEqual(1, 2)
        self.assertIsNone(None)
        self.assertIsNotNone(1)
        self.assertIn(1, [1, 2, 3])
        self.assertNotIn(4, [1, 2, 3])
        self.assertGreater(2, 1)
        self.assertLess(1, 2)
        self.assertGreaterEqual(2, 2)
        self.assertLessEqual(1, 1)

    SERVER = "server_a"

    @unittest.skip("Skipping this test")
    def test_skip(self):
        self.assertEqual(1, 2, "This test should be skipped")

    @unittest.skipIf(SERVER == "server_a", "Skipping this test on server_a")    
    def test_skip_if(self):
        self.assertTrue(False, "This test should be skipped")
        self.skipTest("Skipping this test")