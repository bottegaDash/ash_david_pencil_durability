class Pencil():

    def __init__(self, pencilLength, eraserDurability):
        self.pencilLength = pencilLength
        self.eraserDurability = eraserDurability
        self.pointDurability = 40000


    def pencil_erase(self, text_to_erase):
        for index in range(len(text_to_erase)-1, -1, -1):
            if self.eraserDurability > 0:
                if not text_to_erase[index].isspace():
                    text_to_erase = text_to_erase[:index]+' '+text_to_erase[index+1:]
                    self.eraserDurability -= 1
        return text_to_erase

    def pencil_write(self, text_to_write):
        written_text = ''
        for index in range(0, len(text_to_write)):
            if text_to_write[index].isupper():
                written_text += text_to_write[index]
                self.pointDurability -= 2
            else:
                written_text += text_to_write[index]
                self.pointDurability -= 1
        return written_text
