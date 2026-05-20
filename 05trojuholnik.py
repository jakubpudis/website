a = int(input('Zadajte stranu a: (odvesnu) '))
b = int(input('Zadajte stranu b: (odvesnu) '))
c = int(input('Zadajte stranu c (preponu): '))

if a+b>c and a+c>b and b+c>a:
    print('Tieto strany môžu tvoriť trojuholník :-)')
    pravo = input('Chcete otestovať či je to pravouhlý trojuholník? y/n: ').lower()
    if pravo=='y':
        lava = c*c
        prava = a*a+b*b
        if lava==prava:
            print('Toto je pravouhlý trojuholník')
        else:
            print('Toto nie je pravouhlý trojuholník')
    else:
        input('Stlačte ENTER pre ukončenie')
else:
    print('Tieto strany nemôžu tvoriť trojuholník')
    
