class Pencil():

    POINT_DURABILITY_LOWER_CASE_DEC = 1
    POINT_DURABILITY_UPPER_CASE_DEC = 2
    POINT_DURABILITY_OTHER_CHARACTER_DEC = 1
    PENCIL_LENGTH_DEC = 1
    ERASER_DURABILITY_DEC = 1

    MINIMUM_PENCIL_LENGTH = 0
    MINIMUM_PENCIL_DURIBILITY = 0
    MIMIMUM_POINT_DURABILITY = 0
    MIMIMUM_ERASER_DURABILITY = 0
    MAX_POINT_DURABILITY = 40000

    def __init__(self, pencilLength, eraserDurability):
        self.pencilLength = pencilLength
        self.eraserDurability = eraserDurability
        self.pointDurability = self.MAX_POINT_DURABILITY

    def pencil_erase(self, text_to_erase):
        for index in range(len(text_to_erase)-1, -1, -1):
            if self.eraserDurability > self.MINIMUM_PENCIL_DURIBILITY:
                if not text_to_erase[index].isspace():
                    text_to_erase = text_to_erase[:index]+' '+text_to_erase[index+1:]
                    self.eraserDurability -= self.ERASER_DURABILITY_DEC
        return text_to_erase

    def pencil_write(self, text_to_write):
        written_text = ''
        for index in range(0, len(text_to_write)):
            if text_to_write[index].isspace():
                written_text += text_to_write[index]
            elif self.pointDurability <= self.MIMIMUM_POINT_DURABILITY:
                written_text += ' '
            elif text_to_write[index].isupper():
                written_text = self._update_written_text(written_text, text_to_write, index,
                                                         self.POINT_DURABILITY_UPPER_CASE_DEC)
            elif text_to_write[index].islower():
                written_text = self._update_written_text(written_text, text_to_write, index,
                                                         self.POINT_DURABILITY_LOWER_CASE_DEC)
            else:
                written_text = self._update_written_text(written_text, text_to_write, index,
                                                         self.POINT_DURABILITY_OTHER_CHARACTER_DEC)
        return written_text

    def _update_written_text(self, written_text, text_to_write, index, dec):
        written_text += text_to_write[index]
        self.pointDurability -= dec
        return written_text

    def pencil_sharpen(self):
        if self.pencilLength > self.MINIMUM_PENCIL_LENGTH:
            self.pencilLength -= self.PENCIL_LENGTH_DEC
            self.pointDurability = self.MAX_POINT_DURABILITY
        else:
            self.pointDurability = self.MINIMUM_PENCIL_DURIBILITY
