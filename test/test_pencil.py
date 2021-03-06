from pencil import Pencil
import unittest

class TestPencil(unittest.TestCase):
    def test_create_a_new_pencil_with_lenght_four_and_eraser_durability_four(self):
        p = Pencil(pencilLength=4, eraserDurability=4)
        self.assertEqual(p.pencilLength, 4)
        self.assertEqual(p.eraserDurability, 4)
        self.assertEqual(p.pointDurability, 40000)

    def test_erase_one_letter_update_the_eraser_durability_have_an_empty_string_with_one_white_space(self):
        p = Pencil(pencilLength=4, eraserDurability=4)
        erased_text = p.pencil_erase(text_to_erase='a')
        self.assertEqual(p.eraserDurability, 3)
        self.assertEqual(erased_text, " ")

    def test_erase_two_letter_update_the_eraser_durability_have_an_empty_string_with_two_white_spaces(self):
        p = Pencil(pencilLength=4, eraserDurability=4)
        erased_text = p.pencil_erase(text_to_erase='ab')
        self.assertEqual(p.eraserDurability, 2)
        self.assertEqual(erased_text, "  ")

    def test_erase_five_letters_with_eraser_durability_being_less_than_five_update_the_eraser_durability_to_have_a_string_with_one_letter_and_three_white_spaces(self):
        p = Pencil(pencilLength=4, eraserDurability=4)
        erased_text = p.pencil_erase(text_to_erase='abcde')
        self.assertEqual(p.eraserDurability, 0)
        self.assertEqual(erased_text, "a    ")

    def test_erase_one_letter_with_white_space_update_the_eraser_durability_have_an_empty_string_with_two_white_spaces(self):
        p = Pencil(pencilLength=4, eraserDurability=4)
        erased_text = p.pencil_erase(text_to_erase='a ')
        self.assertEqual(p.eraserDurability, 3)
        self.assertEqual(erased_text, "  ")

    def test_write_one_lowercase_letter_decrease_point_durabilty_by_one(self):
        p = Pencil(pencilLength=4, eraserDurability=4)
        written_text = p.pencil_write(text_to_write="a")
        self.assertEqual(p.pointDurability, 39999)
        self.assertEqual(written_text, "a")

    def test_write_two_lowercase_letter_decrease_point_durabilty_by_two(self):
        p = Pencil(pencilLength=4, eraserDurability=4)
        written_text = p.pencil_write(text_to_write="ab")
        self.assertEqual(p.pointDurability, 39998)
        self.assertEqual(written_text, "ab")

    def test_write_one_uppercase_letter_decrease_point_durabilty_by_two(self):
        p = Pencil(pencilLength=4, eraserDurability=4)
        written_text = p.pencil_write(text_to_write="A")
        self.assertEqual(p.pointDurability, 39998)
        self.assertEqual(written_text, "A")

    def test_write_two_uppercase_letter_decrease_point_durabilty_by_four(self):
        p = Pencil(pencilLength=4, eraserDurability=4)
        written_text = p.pencil_write(text_to_write="AB")
        self.assertEqual(p.pointDurability, 39996)
        self.assertEqual(written_text, "AB")

    def test_write_two_lowercase_letter_two_uppercase_letter_decrease_point_durabilty_by_six(self):
        p = Pencil(pencilLength=4, eraserDurability=4)
        written_text = p.pencil_write(text_to_write="ABcd")
        self.assertEqual(p.pointDurability, 39994)
        self.assertEqual(written_text, "ABcd")

    def test_write_one_lowercase_letter_and_one_whitespace_decrease_point_durabitlity_by_one(self):
        p = Pencil(pencilLength=4, eraserDurability=4)
        written_text = p.pencil_write(text_to_write="a ")
        self.assertEqual(p.pointDurability, 39999)
        self.assertEqual(written_text, "a ")

    def test_write_max_point_durability(self):
        p = Pencil(pencilLength=4, eraserDurability=4)
        f = open('test/input/sample_input.txt', 'r')
        input_text = f.read()
        f.close()
        f = open('test/input/sample_output.txt', 'r')
        output_text = f.read()
        f.close()
        written_text = p.pencil_write(text_to_write=input_text)
        self.assertEqual(p.pointDurability, 0)
        self.assertEqual(written_text, output_text)

    def test_sharpen_pencil_decrease_length_by_one(self):
        p = Pencil(pencilLength=4, eraserDurability=4)
        new_text = p.pencil_write('abcdef')
        self.assertEqual(p.pointDurability, 39994)
        p.pencil_sharpen()
        self.assertEqual(p.pointDurability, 40000)
        self.assertEqual(p.pencilLength, 3)

    def test_sharpen_pencil_by_five_decrease_length_by_four_set_pencil_durability_to_zero(self):
        p = Pencil(pencilLength=4, eraserDurability=4)
        p.pencil_sharpen()
        p.pencil_sharpen()
        p.pencil_sharpen()
        p.pencil_sharpen()
        p.pencil_sharpen()
        self.assertEqual(p.pencilLength, 0)
        self.assertEqual(p.pointDurability, 0)

if __name__ == '__main__':
    unittest.main()
