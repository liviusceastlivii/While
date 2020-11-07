
l = 0
t = 0
tp = 0
ntp = 0
tn = 0
ntn = 0
while l < 12:
    t = eval(input("dati temperatura: "))
    if t <= 0:
        tn += t
        ntn += 1
    else:
        tp += t
        ntp += 1
    l += 1

print("media temperaturii pozitive:", tp / ntp)
print("media temperaturii negative:", tn / ntn)