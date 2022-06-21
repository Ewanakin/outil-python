import hashlib
class ChiffrementHASH:

    def __init__(self,motChiffr):
        self.motChiffr = motChiffr

    def chiffrmentMessage(self):
        return hashlib.sha256(self.motChiffr).hexdigest()