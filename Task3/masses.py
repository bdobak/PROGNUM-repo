masses = [1.9891e+30, 1.8986e+27,
          5.6846e+26, 1.0243e+26, 8.6810e+25,
          5.9736e+24, 4.8685e+24, 6.4185e+23,
          3.3022e+23, 7.349e+22, 1.25e22]
massnew=[]
for i in range(len(masses)):
    if masses[i]>masses[-2]:
        massnew.append(masses[i])

masses.sort()
bigs=slice(0,5)
massbig=masses[bigs]
massavg=sum(massbig)/len(massbig)
print(massavg)
