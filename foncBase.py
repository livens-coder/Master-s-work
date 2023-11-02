print("hello")
#marter srting nimewo 1

chaine= 'Jodia nap MANIPILE chenn kaRAkte'
print(chaine.lower())
k=chaine.split(" ")
print(k)
print(chaine.title())
nouvo_chenn = ''.join([let[0] for let in k if let])
print(nouvo_chenn.lower())

chenn=chaine.replace('a','@')
print(chenn)
nouvo_chenn=chaine[::-1]
print(nouvo_chenn.upper())
print(chaine.index('a'))
chenn=chaine.lower()
endeks=0
for el, karakte in enumerate(chenn):
    if karakte == 'a':
        endeks += el
print("som endeks a nan chenn karakte a se {} ".format(endeks))
lis=[]
for el, karakte in enumerate(chenn):
    if karakte == 'a':
        lis.append(el)
print(lis)

print(chaine.replace(' ', ''))
