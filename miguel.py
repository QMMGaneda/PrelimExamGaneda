# Create a unittest to check if the name is equal to MIGUEL.

import unittest

def name(x):
    return x

class myTest(unittest.TestCase):
    def test(self):

        self.assertEqual(name("MIGUEL"), "MIGUEL")

if __name__ == '__main__':

    unittest.main()