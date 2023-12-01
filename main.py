import forex_python 
from forex_python.converter import CurrencyRates

#creation de variable et de la liste pour l'historique
c = CurrencyRates()
historique=[]

#boucle qui nous demandera a chauqe fois le montant a convertir , les devise et la taux si jamais la devise n'est pas repertoriée
while True:
    try:  
        #l'utilisateur choisis ou non d'ajouter une devise si elle n'existe pas 
        rep=input("voulez vous ajouter une devise ?:(1=oui/2=non) ")
        if rep== "1":
            montant2=float(input("quel est le montant ? : "))
            devise=input("quelle est la premiere devise ? : ")
            devise2=input("quelle est la deuxieme devise ? : ")
            tx=float(input("quelle est le tux de change entre les deux devises ? :"))
            #après avoir prix le montant et le taux le script va les multiplier pour avoir la convertion
            result= montant2 * tx
            #ça va print le resultat avec le nom des devises
            print(f"{montant2} {devise} équivaut à {result:.2f} {devise2}(taux de change : {tx})")
            #ça va ajouter les  anciennes convertion a l'historique
            historique.append(f"{montant2} {devise} équivaut à {result:.2f} {devise2}(taux de change : {tx})")
            #l'utilisateur choisis ou non d'afficher l'historique. Si la réponse est non , c'est la fin du tour de la boucle et elle va recommencer
            reponse=input("voulez vous avoir l'historique ?:(1=oui/2=non)")
            if reponse== "1":
            #si c'est oui , ca va print chaque convertion contenues dans la liste historique et ca sera la fin du tour de la boucle
                print("HISTORIQUE :")
                for i in historique:
                    print(i)
            #fin de boucle
            #si l'utillisateur ne souhaite pas ajouter sa devise , la commande .convert de CurrencyRates va faire automatiquement la convertion des devises les plus connu
        else:
            montant = float(input("Quel montant voulez vous convertir ? : "))
            devises_de = str(input("Quelle est votre devise de départ ?(en majuscule. Ex: USD) : "))
            devise_vers = str(input("Vers quelle devise voulez vous la convertir ?(en majuscule. Ex:EUR) : "))
            #apres avoir demandé les devises et le montant , la commande CurrencyRates.convert va les convertir automatiquement
            resultat = c.convert(devises_de, devise_vers, montant)
            tx_de_change=c.get_rate(devises_de,devise_vers)
            print(f"{montant} {devises_de} équivaut à {resultat:.2f} {devise_vers}(taux de change : {tx_de_change})")
             #ça va ajouter les  anciennes convertion a l'historique
            historique.append(f"{montant} {devises_de} équivaut à {resultat:.2f} {devise_vers}")
             #l'utilisateur choisis ou non d'afficher l'historique. Si la réponse est non , c'est la fin du tour de la boucle et elle va recommencer
            reponse=input("voulez vous avoir l'historique ?:(1=oui/2=non)")
            if reponse== "1":
             #si c'est oui , ca va print chaque convertion contenues dans la liste historique et ca sera la fin du tour de la boucle
                print("HISTORIQUE :")
                for i in historique:
                    print(i)
             #fin de boucle            
    #si une erreur est detecté ca va print "erreur : " avec le motif de l'erreur.      
    except Exception as e:
        print(f"erreur : {e}")
        break



 
