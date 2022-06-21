class Rot:
    def __init__(self,message):
        self.message = message
        self.listChiffr = []

    def messageChiffr(self):
        for i in range(len(self.message)):
            chiffrement = (ord(self.message[i])) - 32
            chiffrement = (chiffrement + 13) % 94
            self.listChiffr.append(chr(chiffrement + 32))
        return "".join(self.listChiffr)

