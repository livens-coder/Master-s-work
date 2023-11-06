import random
import string
from slugify import slugify

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
    vale=int(input("sezi yon nonb: "))
    if vale > 0:
        alfabe=string.ascii_lowercase 
        aleyatwa =''.join(random.choice(alfabe) for let in range(vale))
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
def pemite (val1, val2):
    # val1=int(input("sezi yon vale: "))
    # val2=int(input("sezi yon lot vale: "))
    temp=val1
    val1=val2
    val2=temp
    print("2 vale ou te rantre yo nan yon lot od", (val1,val2))
    return (val1, val2)

pemite(2,4)
print("********************* pati 10 ********************") 

def ekstre_inisyal(non):
    non = non.upper()
    inisyal = ''.join([l[0] for l in non.split()])
    return inisyal

non = "Pierre jean luc kenson"
inisyal = ekstre_inisyal(non)
print(inisyal)

