
#marter srting nimewo 1
print("men fraz kle nou an")
print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
chaine= 'Jodia nap MANIPILE chenn kaRAkte'
print(chaine)
print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n \n")

print("*************************** pati 1 ***********************")

a=chaine.lower()
print("mete tout karakte yo an miniskil :" ,a)
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
print("*************************** pati 10***********************")
k=chaine.replace(' ', '')
t=len(k)
print(f" chenn karakte a san espas  {k} \n kantite karakte li chenn sa vin genyen  {t} \n")


print("------------------------------------------------------------------------------------")
print("nimewo 2")
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
lis_la=[2,3,6,8,9,12,24,94,21,72]
lis=[]
for el in lis_la:
    if el % 3 == 0:
        lis.append(el)
    
print("lis sa divizib selman pa 3", lis) 
print("********************* pati 5 ********************")
lis=[1,2,3,4,5,6,7,8,9]
tay=3 
lis_tuple=[tuple(lis[el:el+tay]) for el in range(0, len(lis),tay)]
print(lis_tuple)
print("********************* pati 6 ********************")
