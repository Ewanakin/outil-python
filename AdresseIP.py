class AdresseIP:

    def __init__(self,adresseIp):
        self.IPstring = adresseIp
        self.addrIP = []

    # test du nombre de point dans la saisie
    def nbOctet(self):
        count = 0
        for i in range(len(self.IPstring)):
            if self.IPstring[i] == ".":
                count += 1
        # si le nombre de point est égale a 3 alors la saisie est bonne
        if count != 3:
            print("L'adresse IP doit seulement contenir 4 octets")
            return False
        else:
            return True

    # conversion de la saisie en int
    def convertIP(self):
        saisieSplit = self.IPstring.split(".")
        try:
            for i in range(len(saisieSplit)):
                self.addrIP.append(int(saisieSplit[i]))
            return True
        # si echec redemander la saisie
        except:
            print("merci de saisir des nombres entiers")
            return False

    # boucle pour tester si l'ip est pas supérieur a 255
    def rangeIP(self):

        for i in range(len(self.addrIP)):
            result = False
            # si index de l'ip est entre 0 et 255 alors l'ip est bonne
            if self.addrIP[i] <= 255 and self.addrIP[i] >= 0:
                result = True
            else:
                print("merci de rentrer une adresse IP entre 0 et 255")
                return False
        return result

    #affichage de la classe de l'ip
    def classeIP(self):
        if self.addrIP[0] < 127:
            print("L'adresse ", self.IPstring, " fait partie de la classe A")
        elif self.addrIP[0] >= 128 and self.addrIP[0] < 191:
            print("L'adresse ", self.IPstring, " fait partie de la classe B")
        elif self.addrIP[0] >= 192 and self.addrIP[0] <= 223:
            print("L'adresse ", self.IPstring, " fait partie de la classe C")
        elif self.addrIP[0] >= 224 and self.addrIP[0] <= 239:
            print("L'adresse ", self.IPstring, " fait partie de la classe D")
        else:
            print("L'adresse ", self.IPstring, " fait partie de la classe E")
        return self.IPstring
