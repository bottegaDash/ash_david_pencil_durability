from pencil import Pencil
import unittest

class TestPencil(unittest.TestCase):
    def test_create_a_new_pencil_with_lenght_four_and_eraser_durability_four(self):
        p = Pencil(pencilLength=4, eraserDurability=4)
        self.assertEqual(p.pencilLength, 4)
        self.assertEqual(p.eraserDurability, 4)
        self.assertEqual(p.pointDurability, 4000)

if __name__ == '__main__':
    unittest.main()
