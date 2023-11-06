

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

print("********************* pati 10 ********************")

print("------------------------------------------------------------------------------------")
