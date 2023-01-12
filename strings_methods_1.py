a=['python']
print(a[1:])
a[0]='P'
print(a)
print(a[0][0])
b='python',
print(dir(str))
n='kriShna PoojA'
print(n.capitalize())#Krishna pooja
print(n.casefold())#krishna pooja
print(n.lower())#krishna pooja
print(n.center(50))#               kriShna PoojA
print(n.center(50,'#'))##############kriShna PoojA##################
print(n.upper())#KRISHNA POOJA
print(n.islower())#False
print(n.isupper())#False
n='krisHna pooJA'
# print(n.title())#Krishna Pooja
print(n.istitle())#False
k=n.encode()
print(k) #b'krisHna pooJA'
print(k.decode()) #krisHna pooJA
k='krishna pooja'
print(k.endswith(''))#True
print(k.endswith(" "))#False
print(k.endswith('a'))#True
k='krishna pooja '
print(k.endswith(''))#True
k='krishna pooja'
print(k.startswith(''))#True
print(k.startswith(' '))#False
print(k.startswith('k'))#True
k='krishna pooja1here'
print(k.index('h'))#4
print(k.index('h',2))#4
print(k.index('h',5))#14
print(k.rindex('a'))#12
# print(k.rindex('l'))#valueError:substring not found





