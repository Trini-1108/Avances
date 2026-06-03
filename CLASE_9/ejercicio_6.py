#Tuplas:

tnumeros = (2, 4, 3)
tnumeros1=(2,4 ,(7, 7, 9) ) #se pueden anidear tuplas
print(tnumeros)
print(tnumeros1)

lnumeros=[1, 2, 3, 2, 5, 2, 7, 8]
tnum= tuple(lnumeros)
print(tuple(tnum))

print("="*50)

for n in tnumeros:
    print(n)

print("="*50)

for m in tnum:
    print(m)

print(tnum.count(2))

print("="*50)
