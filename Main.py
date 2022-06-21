from AdresseIP import AdresseIP
from ScanPort import ScanPort
from Rot import Rot
from SHA256 import ChiffrementHASH
import csv
listPort = []
point = False
convert = False
nombre = False


choixApplication = input("Que souhaitez faire ? \n"
                         "1 - Scan de port avec Controle de saisie sur l'adresse IP\n"
                         "2 - Chiffrement d'un message "
                         "3 - Lecture fichier CSV :")
if choixApplication == "1":
    ###############################################################################
    #Controle de Saisie pour la saisie de l'adresse IP
    while point == False or convert == False or nombre == False:
        saisieIP = input("saisir l'ip : ")
        # création de l'objet adressse
        addresse = AdresseIP(saisieIP)
        # appel des 3 test (conversion de la saisie, test du nombre d'octets et taille de l'IP
        convert = addresse.nbOctet()
        nombre = addresse.convertIP()
        point = addresse.rangeIP()
    # affichage de la classe de l'IP
    adresseIP = addresse.classeIP()
    ###############################################################################
    #si la saisie est ok on passe au scan de port
    # choix du mode de scan
    choixModeScan = input("saisir le mode de scan : \n"
                      "1 - scan de port avec saisie des ports\n"
                      "2 - scan de port avec choix de l'interval des ports\n"
                      "mode n° : ")
    # création de l'objet scan
    scan = ScanPort(adresseIP)
    ###############################################################################
    #si choix == 1 alors faire un sacn de port avec saisie des ports
    if choixModeScan == "1":
        # saisie des port dans la liste
        saisiePort = input("saisir la liste des ports \n"
                           "exemple : 80 4444 5555 2563 : ")
        # la fonction split sépare la chaine de caractère saisie
        recup = saisiePort.split()
        # déclaration pour chaque éléments de la liste en int
        for i in range(len(recup)):
            listPort.append(int(recup[i]))
        # appel de la fonction netscanListe avec l'argument host==Ip
        scan.netcatListe(listPort)
    ###############################################################################
    #si choix == 2 alors faire un scan de port avec un interval
    elif choixModeScan == "2":
        # saisie de la valeur Minimale
        min = int(input("Saisir la valeur Minimale : "))
        # saisie de la valeur Maximale
        max = int(input("Saisir la valeur Maximale : "))
        # appel de la fonction netcatInter avec les arguments host==adresse IP, min==valeur min et max== valeur max
        scan.netcatInter(min, max)
    #appel de la fonction affichage Port de l'objet scan
    scan.affichagePort()

elif choixApplication == "2":
    #choix du mode de chiffrment en sha 256 ou rot 13
    choixModeChiffr = input("Que souhaitez faire ? \n"
                             "1 - Chiffrement du message avec ROT13\n"
                             "2 - Chiffrement du message avec SHA256 : ")
    motChiffr = input("saisir le mot à chiffrer avec le ROT : ")
    if choixModeChiffr == "1":
        chiffrRot = Rot(motChiffr)
        motChiffr = chiffrRot.messageChiffr()
        print("Le message chiffré avec ROT 13 est : ", motChiffr)
    elif choixModeChiffr == "2":
        motChiffrEncode = motChiffr.encode()
        chiffrHash = ChiffrementHASH(motChiffrEncode)
        resultChiffr = chiffrHash.chiffrmentMessage()
        print(resultChiffr)
elif choixApplication == "3":
    file = open(r"test.csv")
    viewCSV = csv.reader(file)
    for row in viewCSV:
        print(row)



