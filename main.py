import forex_python 
from forex_python.converter import CurrencyRates

c = CurrencyRates()
historique=[]

while True:
    try:  
        rep=input("voulez vous ajouter une devise ?:(1=oui/2=non) ")
        if rep== "1":
            montant2=float(input("quel est le montant ? : "))
            devise=input("quelle est la premiere devise ? : ")
            devise2=input("quelle est la deuxieme devise ? : ")
            tx=float(input("quelle est le tux de change entre les deux devises ? :"))
            result= montant2 * tx
            print(f"{montant2} {devise} équivaut à {result:.2f} {devise2}(taux de change : {tx})")
            historique.append(f"{montant2} {devise} équivaut à {result:.2f} {devise2}(taux de change : {tx})")
            reponse=input("voulez vous avoir l'historique ?:(1=oui/2=non)")
            if reponse== "1":
                print("HISTORIQUE :")
                for i in historique:
                    print(i)
        else:
            montant = float(input("Quel montant voulez vous convertir ? : "))
            devises_de = str(input("Quelle est votre devise de départ ?(en majuscule. Ex: USD) : "))
            devise_vers = str(input("Vers quelle devise voulez vous la convertir ?(en majuscule. Ex:EUR) : "))
            resultat = c.convert(devises_de, devise_vers, montant)
            tx_de_change=c.get_rate(devises_de,devise_vers)
            print(f"{montant} {devises_de} équivaut à {resultat:.2f} {devise_vers}(taux de change : {tx_de_change})")
            historique.append(f"{montant} {devises_de} équivaut à {resultat:.2f} {devise_vers}")

            reponse=input("voulez vous avoir l'historique ?:(1=oui/2=non)")
            if reponse== "1":
                print("HISTORIQUE :")
                for i in historique:
                    print(i)
           
    except Exception as e:
        print(f"erreur : {e}")
        break



 
