import random
import string
from slugify import slugify
#marter srting nimewo 1
print("men fraz kle nou an")
print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
chaine= 'Jodia nap MANIPILE chenn kaRAkte'
print(chaine)
print("------------------------------------------------------------------------------------")
print("@@@@@@@@@@@@@@@@@@@ nimewo 1 ---- Master string --- @@@@@@@@@@@@@@@@@")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

print("*************************** pati 1 ***********************")

a=chaine.lower()
print("mete tout karakte yo an miniskil :\n" ,a)
print("*************************** pati 2 ***********************")
k=chaine.split(" ")
print("koupe chenn nan tout kote ki gen espas :\n", k)
print("*************************** pati 3 ***********************")
b=chaine.title()
print('tout premye let chak mo an majiskil :\n', b)
print("*************************** pati 4 ***********************")
nouvo_chenn = ''.join([let[0] for let in k if let])
c=nouvo_chenn.lower()
print('ekipere premye let chak mo =>: \n', c)
print("*************************** pati 5 ***********************")
chenn=chaine.replace('a','@')
print('Ranplase tout karakte <a> ki nan yon chenn pa <@> : \n', chenn)
print("*************************** pati 6 ***********************")
nouvo_chenn=chaine[::-1]

print("Mete yon chenn karakte devan deye, answit mete l an majiskil : \n", nouvo_chenn.upper())
print("*************************** pati 7***********************")
print("endeks premye karakte <a> ki nan yon chenn \n", chaine.index('a'))
print("*************************** pati 8 ***********************")
chenn=chaine.lower()
endeks=0
for el, karakte in enumerate(chaine):
    if karakte == 'a' or karakte == 'A':
        endeks += el
print("som endeks a nan chenn karakte a se \n", endeks)
print("*************************** pati 9 ***********************")
lis=[]
for el, karakte in enumerate(chaine):
    if karakte == 'a' or karakte == 'A':
        lis.append(el)
print("yon lis ki gen endeks tout karakte 'a' ki nan yon chenn \n:", lis)
print("*************************** pati 10 ***********************")
k=chaine.replace(' ', '')
t=len(k)
print(f" chenn karakte a san espas  {k} \n kantite karakte li chenn sa vin genyen  {t} \n")
print("------------------------------------------------------------------------------------")
print("@@@@@@@@@@@@@@@@@@@ nimewo 2 ---- Master list --- @@@@@@@@@@@@@@@@@")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

print("********************* pati 1 ********************")
k=[]
for i in range(2):
    a = int(input("rantre yon nonb pe : "))
    while a % 2 != 0:
        print("nonb ou rantre apa divizib pa 2. Réessayez.")
        a = int(input("rantre yon nonb pe  : "))
    k.append(a)
print("sa se lis eleman ou sezi a ki tou dizib pa 2", k)
print("********************* pati 2 ********************")
a= ''.join(map(str,k))
print("men lis la sou fom chenn karakte", a)
print("********************* pati 3 ********************")
lis_chenn=['nap', 'travay', 'python']
el_majis= [el.upper() for el in lis_chenn]
print("chenn nou an an majiskil ", el_majis) 
print("********************* pati 4 ********************")
lis_la=[2,3,6,8,9,12,8,94,21,72,3,12,94]
lis=[]
for i, el in enumerate (lis_la):
    if el % 3 == 0:
        if lis_la.count(i)==0:
            lis.append(i)
print("endeks eleman nan lis mwen an ki divizib pa 3 \n", lis)
    
print("lis sa divizib selman pa 3", lis) 
print("********************* pati 5 ********************")
lis=[1,2,3,4,5,6,7,8,9]
tay=3 
lis_tuple=[tuple(lis[el:el+tay]) for el in range(0, len(lis),tay)]
print(lis_tuple)
print("********************* pati 6 ********************")
print("lis mwen an san doublon ", list(set(lis_la)))
print("********************* pati 7 ********************")
print(lis)
print(lis_la)
lis_fizyone=lis + lis_la
print("fizyon de lis sa yo se ", lis_fizyone)
print("********************* pati 8 ********************")
print("lis fizyone a san doublon ", list(set(lis_fizyone)))
print("********************* pati 9 ********************")
diksyone={'a':2, 'b':3, 'c':5, 'd':7, 'e':9, 'f':12}
print(diksyone)
print("lis ki gen kle nan diksyone an ", list(diksyone.keys()))
print("lis ki gen vale nan diksyone an ", list(diksyone.values()))
print("********************* pati 10 ********************")
print( "lis1",lis_la)
print("lis2", lis)
print("lis3", lis_chenn)
lis_trip=lis+lis_chenn+lis_la
print("fizyon 3 lis ansanm ", list(set(lis_trip)))
print("------------------------------------------------------------------------------------")
print("@@@@@@@@@@@@@@@@@@@ nimewo 3 ---- Master dict --- @@@@@@@@@@@@@@@@@")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ \n \n")
print("********************* pati 1 ********************")
diksyone={'q':2, 'w':12, 'e':'hello', 'r':'hi','t':21 }
k=[]
for kle, vale in diksyone.items():
    k.append(vale)
print("men lis vale ki genyen nan diksyone mwen an:\n", k)
print("********************* pati 2 ********************")
q=input("rantre yon vale: ")
if len(q)>= 2 and q[0]=='{' and q[-1]=='}':
    print("vale ou an gen akolade devan e deye ", q)
else:
    print("vale ou an pa nan mitan akolad ", q)
print("********************* pati 3 ********************")
for kle in diksyone:
     print("kle yo", kle)
print("********************* pati 4 ********************")
for kle in diksyone.values():
     print("kle yo", kle)
print("********************* pati 5 ********************")
diksyone={'a':2, 'b':3, 'c':5, 'm':'Hello', 'e':9, 'f':12}
dik={}
for el, vale in diksyone.items():
    dik[el]=vale
print("kopi diksyone mwen an: ", dik)
print("********************* pati 6 ********************")
n_diksyone = {'a': 'good', 'wi': 5, 'm': 'Hello', 'e': 9, 'f': 12}
for cle, valeur in n_diksyone.items():
    if isinstance(valeur, str):
        n_diksyone[cle] = "_" + valeur + "_"

print(n_diksyone)
print("********************* pati 7 ********************")
n_diksyone = {'a': 'good', 'wi': 5, 'm': 'Hello', 'e': 9, 'f': 12}

kle_siprime = []
for kle, vale in n_diksyone.items():
    if isinstance(vale, str):
        kle_siprime.append(kle)
for kle in kle_siprime:
    del n_diksyone[kle]
print("diksyone mwen an se chenn karakte \n", n_diksyone)
print("********************* pati 8 ********************")
diksyone = {"a": 1, "b": 2}
lis_tipl = [(kle, vale) for kle, vale in diksyone.items()]
print("kle, vale diksyon yo nan yon tuple \n", lis_tipl)
print("********************* pati 9 ********************")

lis_tipl = [("a", 1), ("b", 2)]
diksyone = dict(lis_tipl)
print("konveti tipl an diksyone \n", diksyone)
# print("********************* pati 10 ********************")
print("------------------------------------------------------------------------------------")
print("@@@@@@@@@@@@@@@@@@@ nimewo 4 ---- Master fonc --- @@@@@@@@@@@@@@@@@")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ \n \n")
print("********************* pati 1 ********************")
def enves_mo():
    mo=input("sezi yon mo: ")
    if mo:
        print("mo ou rantre a se: ", mo[::-1]) 

enves_mo()
print("********************* pati 2 ********************")

def alfabe_aleatwa():
    vale=int(input("sazi yon nonb: "))
    if vale > 0:
        alfabe=string.ascii_lowercase 
        aleyatwa =' '.join(random.choice(alfabe) for let in range(vale))
        print("kelke let aleyatwa: ", aleyatwa)
        
alfabe_aleatwa()
print("********************* pati 3 ********************")
def alfa_aleya(vale):
    
    alfabe = string.ascii_lowercase
    if vale > 0 and vale <= len(alfabe):  
        aleyatwa = ' '.join(random.sample(alfabe, vale))  
        print("Kelke let aleyatwa:", aleyatwa)
        return aleyatwa
    else:
        print("Vale a dwe antre nan antèval 1 ak", len(alfabe))
n = int(input("Sazi yon nonb: "))
alfa_aleya(n)

print("********************* pati 4 ********************")
def analfa_aleya(vale):
    
    alfabe = string.ascii_letters + string.digits
    if vale > 0 and vale <= len(alfabe):  
        aleyatwa = ' '.join(random.sample(alfabe, vale))  
        print("Kelke let aleyatwa:", aleyatwa)
        return aleyatwa
    else:
        print("Vale a dwe antre nan antèval 1 ak", len(alfabe))
n = int(input("Sazi yon nonb: "))
analfa_aleya(n)
print("********************* pati 5 ********************")
def trans_slug():
    chenn= 'nap fristal ak python sa'
    slug=slugify(chenn)
    print("transfomasyon chenn nan an slug: ", slug)

trans_slug()
print("********************* pati 6 ********************")
def separe_chenn():
    chenn = 'nap fristal ak python sa'
    chenn_separe = ', '.join(chenn)
    print(chenn_separe)

separe_chenn()

print("********************* pati 7 ********************")

def kripte_mo():
    mo = input("Antre yon mo pou kripte: ")
    mo = mo.upper()  # Konvèti mo nan tout kapital
    kripte = '-'.join([str(ord(lettre) - ord('A')) for lettre in mo if lettre.isalpha()])
    print("mo kripte a se: ", kripte)
    return kripte

kripte_mo()
print("********************* pati 8 ********************") 
def dekripte_ko():
    ko_kripte = input("Antre kòd kripte ou an sa tire: ")
    tèks = ''
    
    for kod in ko_kripte.split('-'):
        if kod.isdigit():
            tèks += chr(int(kod) + ord('A'))
        else:
            tèks += kod
    
    print("Tèks anvan kriptaj la: ", tèks)
    return tèks

dekripte_ko()

print("********************* pati 9 ********************") 
def pemite ():
    val1=int(input("sezi yon vale: "))
    val2=int(input("sezi yon lot vale: "))
    temp=val1
    val1=val2
    val2=temp
    print("2 vale ou te rantre yo nan yon lot od", (val1,val2))
    return (val1, val2)

pemite()
print("********************* pati 10 ********************") 

def ekstre_inisyal(non):
    non = non.upper()
    inisyal = ''.join([l[0] for l in non.split()])
    return inisyal

non = "Pierre jean luc kenson"
inisyal = ekstre_inisyal(non)
print(inisyal)

