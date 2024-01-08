# -*- coding: utf-8 -*-



alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] #Notre liste d'alphabet en minuscule
alphabet2 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] #Notre liste d'alhabet en majuscule

for x in range(len(alphabet)): #On parcours notre alphabet1 et alphabet2
  alphabet.append(alphabet[x]) ##On append notre alphabet en minuscule
  alphabet2.append(alphabet2[x]) #On append notre alphabet en majuscule


# Calcul du pgcd de a et b
def pgcd(a,b): 
    while b!=0: #Boucle tant que b différent de 0
        a,b=b,a%b #On change le a avec le b ensuite on fait a%b
    return a #On retourne a


# Fonction de chiffrement affine
def chiffrementAffine(a,b,L):
        if L in alphabet2: #Si L est une lettre en majuscule
          x=alphabet2.index(L) #x prend l'indice de la lettre dans l'alphabet en majuscule
          y=(a*x+b)%26 #y prend la valeur de la lettre en majuscule L après chiffrement affine 
          return alphabet2[y] #On retourne la lettre chiffrée en majuscle
        elif L in alphabet : #Sinon Si L est une lettre en minuscle
            x=alphabet.index(L) #x prend l'indice de la lettre dans l'alphabet en minuscule
            y=(a*x+b)%26 #y prend la valeur de la lettre en minsucle L après chiffrement affine 
            return alphabet[y] #On retourne la lettre chiffrée en minuscule
        else :       #Sinon c'est un symbole
            return L #On retourne le symbole tout simplement sans rien effectuer
        
        
# Calcul de l'inverse d'un nombre modulo 26
def inverse(a):
        x=0 #x prend la valeur 0 au départ
        while (a*x%26!=1): #Boucle tant que a*x%26 n'est pas différent de 1
                x=x+1 #x prend la valeure de x + 1 tant que la boucle est vrai
        return x #On retourne la valeure de x
   
    
#Calcul de l'inverse d'un nombre modulo 26 avec Euclide Etendu
def euclide(a):
    # Initialisation
    b=26 #b prend la valeur 26 
    d,u,v,d1,u1,v1=a,1,0,b,0,1 #on initialiste les 1ere cases pour effectuer l'algorithme d'euclide etendu
    # Calcul
    while d1!=0: #Boucle qui s'arrete seulement lorsque d = 0
        q=d//d1 #q prend la valeur du reste de la division euclidienne de d par d1
        d,u,v,d1,u1,v1=d1,u1,v1,d-q*d1,u-q*u1,v-q*v1 #On applique la formule du cours
    x=u #x prend la valeur de l'inverse de a
    return x #On retourne l'inverse de a


# Fonction de déchiffrement
def dechiffrementAffine(a,b,L):
    if L in alphabet: #Si L est une lettre en minuscule
        x=alphabet.index(L) #x prend l'indice de la lettre dans l'alphabet en minuscule
        y=(inverse(a)*(x-b))%26 #y prend la valeur de la lettre en minsucle L après déchiffrement affine
        return alphabet[y] #On retourne la lettre déchiffrée en minuscule
    elif L in alphabet2 : #Sinon si L est une lettre en majuscule
        x=alphabet2.index(L) #x prend l'indice de la lettre dans l'alphabet en majuscule
        y=(inverse(a)*(x-b))%26 #y prend la valeur de la lettre en majuscule L après déchiffrement affine
        return alphabet2[y] #On retourne la lettre déchiffrée en majuscle
    else :              #Sinon c'est un symbole non chiffré
        return L        #On retourne le symbole
      
                
# Affichage du mot chiffré
def crypt(M,a,b):
    if (pgcd(a,26)==1): #Si le pgcd de a et 26 est égale à 1
        mot = [] #On initialiste un string vide
        for i in range(0,len(M)): #Boucle qui parcours la longeur du message à chiffré
                mot.append(chiffrementAffine(a,b,M[i])) #mot prend à chaque parcours la lettre chiffré après appel à la fonction chiffrementAffine et on la met à la fin de mot
        return "".join(mot) #On retourne le mot avec toute les lettres ou symboles chiffrés
    else: #Sinon il y a une erreur
        return "Chiffrement impossible. Veuillez choisir un nombre a premier avec 26." #On retourne que a n'est pas premier avec 26


# Affichage du mot déchiffré
def decrypt(M,a,b):
    if (pgcd(a,26)==1): #Si le pgcd de a et 26 est égale à 1
        mot = [] #On initialiste un string vide
        for i in range(0,len(M)):  #Boucle qui parcours la longeur du message à déchiffré
          mot.append(dechiffrementAffine(a,b,M[i])) #mot prend à chaque parcours la lettre déchiffré après appel à la fonction déchiffrementAffine et on la met à la fin de mot
        return "".join(mot) #On retourne le mot avec toute les lettres ou symboles déchiffrés
    else: #Sinon il y a une erreur
        return "Déchiffrement impossible. Le nombre a n'est pas premier avec 26." #On retourne que a n'est pas premier avec 26


#Fonction pour tester notre programme

print("1: chiffrement d'un message")
print("2: dechiffrement d'un message")
choix = int(input("Entrez votre choix : "))

if choix == 1:
    message1 = input("Entrez le message a chiffrer:  ")
    a = int(input("Entrez la cle a:  "))
    b = int(input("Entrez la cle b:  "))
    msg_chiffre1 = crypt(message1, a, b) #On chiffre le message1
    print('Le message chiffré 1 est  : \n', msg_chiffre1)
    
elif choix == 2:
    message1 = input("Entrez le message a dechiffrer:  ")
    a = int(input("Entrez la cle a:  "))
    b = int(input("Entrez la cle b:  "))
    msg_dechiffre1 = decrypt(message1,a,b) #On chiffre le message1
    print('Le message déchiffré 1 est : \n', msg_dechiffre1)   




