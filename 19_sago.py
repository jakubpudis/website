#sago + sano  = felic


print ('SAGO + SANO = FELIC')
f=1
p=0
for s in range (5,10):
    for a in range (0,10):
        if (a!=s) and (a!=f):
            for g in range (0,10):
                if (g!=s) and (g!=a) and (g!=f):
                    for o in range (0,10):
                        if (o!=s) and (o!=a) and (o!=g) and (o!=f):
                            for n in range (0,10):
                                if(n!=s) and (n!=a) and (n!=g) and (n!=o) and (n!=f):
                                    for e in range (0,10):
                                        if (e!=s) and (e!=a) and (e!=g) and (e!=o) and (e!=n) and (e!=f):
                                            for l in range (0,10):
                                                if (l!=s) and (l!=a) and (l!=g) and (l!=o) and (l!=n) and (l!=e) and (l!=f):
                                                    for i in range (0,10):
                                                        if (i!=s) and (i!=a) and (i!=g) and (i!=o) and (i!=n) and (i!=e) and (i!=l) and (i!=f):
                                                            for c in range (0,10):
                                                                if (c!=s) and (c!=a) and (c!=g) and (c!=o) and (c!=n) and (c!=e) and (c!=l) and (c!=i) and (c!=f):
                                                                    v1=o+10*g+100*a+1000*s
                                                                    v2=o+10*n+100*a+1000*s
                                                                    v3=c+10*i+100*l+1000*e+10000*f
                                                                    if ((v1+v2)==v3):
                                                                        p=p+1
                                                                        print(f"riesenie cislo {p}")
                                                                        print(f" S= {s} , A= {a}, G= {g} O= {o}, N= {n}, F= {f},  E= {e}, L= {l}, I= {i}, C= {c}")
                                                                        print(f" {s}{a}{g}{o} + {s}{a}{n}{o} = {f}{e}{l}{i}{c}")
print(f"Koniec hladania - uloha ma {p} rieseni")
