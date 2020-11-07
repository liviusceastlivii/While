n=eval(input("dati numarul maxim: "))
i=1
suma=0
produs=1
media=0
nnr=0
while(i <= n):
    suma += i
    produs *= i
    nnr += 1
    media = suma / nnr
    i += 1

print(suma)
print(produs)
print( media) 