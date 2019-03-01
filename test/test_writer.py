from write import Write
import unittest

class TestWriter(unittest.TestCase):
    def test_write_one_string_on_paper(self):
        w = Write()
        w.write_on_paper('She sells sea shells')
        self.assertEqual(w.paper, 'She sells sea shells')

if __name__ == '__main__':
    unittest.main()
