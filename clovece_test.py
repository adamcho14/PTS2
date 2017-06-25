import clovece_classes
import unittest

class test(unittest.TestCase):

    def test_kolizia(self):
        tested = clovece_classes.Clovece()
        tested.tah()
        self.assertEqual(tested.kolizia(0), (-1, -1))

    def test_tah(self):
        tested = clovece_classes.Clovece()
        self.assertEqual(tested.tah(), 2)

    def test_hra(self):
        tested = clovece_classes.novaHra()
        self.assertEqual(tested.hraj(), (12, 3))

if __name__ == "__main__":
    unittest.main()

