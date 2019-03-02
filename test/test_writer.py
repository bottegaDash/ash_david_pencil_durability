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

    def test_sharpen_pencil_decrease_length_by_one(self):
        w = Write()
        w.write_on_paper('abcdef')
        self.assertEqual(w.pencil.pointDurability, 39994)
        w.sharpen_pencil()
        self.assertEqual(w.pencil.pointDurability, 40000)
        self.assertEqual(w.pencil.pencilLength, 3)

    def test_erase_word_the_last_occurance_of_the_word_should_be_repalced_by_spaces(self):
        w = Write()
        w.write_on_paper(desired_text_to_write="How much wood would a woodchuck chuck if a woodchuck could chuck wood?")
        w.erase('chuck')
        self.assertEqual(w.paper, "How much wood would a woodchuck chuck if a woodchuck could       wood?")

    def test_erase_word_the_last_and_second_to_last_occurance_of_the_string_the_word_should_be_repalced_by_spaces(self):
        w = Write()
        w.write_on_paper(desired_text_to_write="How much wood would a woodchuck chuck if a woodchuck could chuck wood?")
        w.erase('chuck')
        w.erase('chuck')
        self.assertEqual(w.paper, "How much wood would a woodchuck chuck if a wood      could       wood?")

    def test_edit_replacec_apple_with_onion(self):
        w = Write()
        w.write_on_paper(desired_text_to_write="An apple a day keeps the doctor away")
        index = w.erase('apple')
        w.edit(index, 'onion')
        self.assertEqual(w.paper, "An onion a day keeps the doctor away")

if __name__ == '__main__':
    unittest.main()
