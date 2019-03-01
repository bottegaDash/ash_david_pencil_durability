from write import Write
import unittest

class TestWriter(unittest.TestCase):
    def test_write_one_string_on_paper(self):
        w = Write()
        w.write_on_paper('She sells sea shells')
        self.assertEqual(w.paper, 'She sells sea shells')

    def test_write_two_strings_on_paper_both_strings_should_be_concatinated(self):
        w = Write()
        w.write_on_paper('She sells sea shells')
        w.write_on_paper(' down by the sea shore')
        self.assertEqual(w.paper, 'She sells sea shells down by the sea shore')

if __name__ == '__main__':
    unittest.main()
