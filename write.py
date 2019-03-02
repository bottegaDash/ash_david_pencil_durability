from pencil import Pencil

class Write():
    def __init__(self):
        self.pencil = Pencil(pencilLength = 4, eraserDurability = 10)
        self.paper = ''

    def write_on_paper(self, desired_text_to_write):
        text_to_write = self.pencil.pencil_write(desired_text_to_write)
        self.paper += text_to_write

    def sharpen_pencil(self):
        self.pencil.pencil_sharpen()

    def erase(self, desired_text_to_erase):
        text_to_erase = self.pencil.pencil_erase(text_to_erase=desired_text_to_erase)
        index = self.paper.rfind(desired_text_to_erase)
        self.paper = self.paper[:index] + text_to_erase + self.paper[index+len(text_to_erase):]
        return index

    def edit(self, index, text_to_add):
        self.paper = self.paper[:index] + text_to_add + self.paper[index+len(text_to_add):]
