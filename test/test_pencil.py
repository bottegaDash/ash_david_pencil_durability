from pencil import Pencil
import unittest

class TestPencil(unittest.TestCase):
    def test_create_a_new_pencil_with_lenght_four_and_eraser_durability_four(self):
        p = Pencil(pencilLength=4, eraserDurability=4)
        self.assertEqual(p.pencilLength, 4)
        self.assertEqual(p.eraserDurability, 4)
        self.assertEqual(p.pointDurability, 4000)

    def test_erase_one_letter_update_the_eraser_durability_have_an_empty_string_with_one_white_space(self):
        p = Pencil(pencilLength=4, eraserDurability=4)
        erased_text = p.pencil_erase(text_to_erase='a')
        self.assertEqual(p.eraserDurability, 3)
        self.assertEqual(erased_text, " ")

    def test_erase_two_letter_update_the_eraser_durability_have_an_empty_string_with_two_white_space(self):
        p = Pencil(pencilLength=4, eraserDurability=4)
        erased_text = p.pencil_erase(text_to_erase='ab')
        self.assertEqual(p.eraserDurability, 2)
        self.assertEqual(erased_text, "  ")


    def test_erase_five_letters_with_eraser_durability_being_less_than_five_update_the_eraser_durability_to_have_a_string_with_one_letter_and_three_white_spaces(self):
        p = Pencil(pencilLength=4, eraserDurability=4)
        erased_text = p.pencil_erase(text_to_erase='abcde')
        self.assertEqual(p.eraserDurability, 0)
        self.assertEqual(erased_text, "a    ")

if __name__ == '__main__':
    unittest.main()
