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