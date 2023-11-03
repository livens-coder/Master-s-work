
#marter srting nimewo 1
print("nap komanse ak fraz anba a")
chaine= 'Jodia nap MANIPILE chenn kaRAkte'
print(chaine)
print("-----------------------------------------------------")

a=chaine.lower()
print("mete tout karakte yo an miniskil =>:" ,a)
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
for el, karakte in enumerate(chaine):
    if karakte == 'a' or karakte == 'A':
        endeks += el
print("som endeks a nan chenn karakte a se =>: ", endeks)
lis=[]
for el, karakte in enumerate(chaine):
    if karakte == 'a' or karakte == 'A':
        lis.append(el)
print("yon lis ki gen endeks tout karakte 'a' ki nan yon chenn => :", lis)

k=chaine.replace(' ', '')
t=len(k)
print(" chenn karakte a san espas =>  {},  kantite karakte li chenn sa vin genyen => {}".format(k,t))

print("nimewo 2")
print("------------------------------------------------: ")
k=[]

for i in range(0,2):
    a=int(input("rantre kek n: "))
    if a%2 ==0:
        k.append(a)
        
    else:
        a=int(input("eseye anko nonb ou an pa divizib pa 2: "))
        
print("sa se lis eleman ou sezi a ki tou dizib pa 2", k)
## pati 2
a= ''.join(map(str,k))
print("men lis la sou fom chenn karakte", a)

