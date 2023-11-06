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