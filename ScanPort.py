import socket

class ScanPort:
    def __init__(self,host):
        self.host = host
        self.portOpen = []
        self.listPort = []

    #valide
    def connexion(self, host, port):
        # tentative de connexion aux ports
        try:
            # création du socket avec IPV4 et TCP
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # delais du test de connexion
            s.settimeout(0.5)
            # connexion a l'IP et au port en fonction de l'index de la liste
            s.connect((host, port))
            # fermeture du socket-
            s.close()
            # ajoutdu port dans la liste portOpen en fonction de l'index i de la liste
            self.portOpen.append(port)
        # fermeture du port si echec de la connexion au port
        except:
            s.close()

    #VALIDE
    def netcatListe(self,listPort):
        # affichage de la durée de l'opération
        # execution de la boucle en fontion du nombre de valeurs dans la liste
        for i in range(len(listPort)):
            # appel de la fonction de connexion
            ScanPort.connexion(self, self.host, listPort[i])

    #valide
    def netcatInter(self,min, max):
        # affichage de la durée de l'opération
        # boucle pour effectuer l'interval demandé
        for i in range(min, max):
            # appel de la fonction connexion
            ScanPort.connexion(self, self.host, i)

    #valide
    def affichagePort(self):
        # affichage des port ouverts
        if len(self.portOpen) > 0:
            for i in range(len(self.portOpen)):
                print("Le port :", self.portOpen[i], " est ouvert")
        # si aucun port n'est ouvert alors afficher aucun port n'est ouvert
        else:
            print("aucun port n'est ouvert")