
#marter srting nimewo 1
print("nap komanse ak fraz anba a")
chaine= 'Jodia nap MANIPILE chenn kaRAkte'
print(chaine)
print("-----------------------------------------------------")

a=chaine.lower()
print("mete tout karakte yo an miniski =>:" ,a)
k=chaine.split(" ")
print("koupe chenn nan tout kote ki gen espas =>:", k)
b=chaine.title()
print('tout premye let chak mo an majiskil =>:', b)
nouvo_chenn = ''.join([let[0] for let in k if let])
c=nouvo_chenn.lower()
print('ekipere premye let chak mo =>: ', c)

chenn=chaine.replace('a','@')
print('Ranplase tout karakte <a> ki nan yon chenn pa <@> =>: ', chenn)
nouvo_chenn=chaine[::-1]

print("Mete yon chenn karakte devan deye, answit mete l an majiskil =>: ", nouvo_chenn.upper())
print("endeks premye karakte <a> ki nan yon chenn =>:", chaine.index('a'))
chenn=chaine.lower()
endeks=0
for el, karakte in enumerate(chenn):
    if karakte == 'a':
        endeks += el
print("som endeks a nan chenn karakte a se =>: ", endeks)
lis=[]
for el, karakte in enumerate(chenn):
    if karakte == 'a':
        lis.append(el)
print("yon lis ki gen endeks tout karakte 'a' ki nan yon chenn => :", lis)

k=chaine.replace(' ', '')
t=len(k)
print(" chenn karakte a san espas =>  {},  kantite karakte li chenn sa vin genyen => {}".format(k,t))

## nimewo 2
print("nap komanse nan pati 2 a la: ")