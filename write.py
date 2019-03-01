from pencil import Pencil

class Write():
    def __init__(self):
        self.pencil = Pencil(pencilLength = 4, eraserDurability = 4)
        self.paper = ''

    def write_on_paper(self, desired_text_to_write):
        text_to_write = self.pencil.pencil_write(desired_text_to_write)
        self.paper += text_to_write
