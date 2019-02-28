class Pencil():

    def __init__(self, pencilLength, eraserDurability):
        self.pencilLength = pencilLength
        self.eraserDurability = eraserDurability
        self.pointDurability = 4000


    def pencil_erase(self, text_to_erase):
        for index in range(len(text_to_erase)-1, -1, -1):
            if self.eraserDurability > 0:
                text_to_erase = text_to_erase[:index]+' '+text_to_erase[index+1:]
                self.eraserDurability -= 1
        return text_to_erase
