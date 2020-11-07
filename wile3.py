n=0
suma=0
while ((n%2 == 0) or (n% 3 != 0)):
    n=eval(input("dati numarul:"))
    if n%2==0:
        suma+=n
print(suma)
