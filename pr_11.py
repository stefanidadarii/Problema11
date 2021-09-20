n = int(input('Introduceti n: '))
lista=[]
if n<10:
    print('Introduceti', n, ' elemente pentru vectorul creat:')
    for i in range(0, n):
        n1=int(input('Dati elementul: '))
        lista.extend([n1])
    print(lista)
    l1=lista.copy()
    print('b) afişează pe ecran numerele în ordinea inversă a introducerii în calculator:', l1[::-1])
    print('c) sortează componentele tabloului în ordine descrescătoare: ')
    l1.sort(reverse=True)
    print(l1)
    print('d) afişează pe ecran doar componentele pare: ')
    d=[]
    for i in range(0,len(lista)):
        if lista[i]%2==0:
            d.append(lista[i])
    print(d)
    print('e) afişează pe ecran media aritmetică a componentelor pare:')
    e=sum(d)/len(d)
    print(e)
    print('f) afişează pe ecran doar componentele impare:')
    f=[]
    for i in range(0,len(lista)):
        if lista[i]%2!=0:
            f.append(lista[i])
    print(f)    
    x=int(input('x ='))
    y=int(input('y ='))
    print('g) afişează pe ecran doar componentele care sunt mai mari ca x şi nu sunt divizibile cu y:')
    g=[]
    for i in range(0,len(lista)):
        if (lista[i]>x) and (lista[i]%y != 0):
            g.append(lista[i])
    print(g)
    print('h) afişează pe ecran doar componentele care sunt mai mari ca x şi mai mici decât y:')
    h=[]
    for i in range(0,len(lista)):
        if (lista[i]>x) and (lista[i]<y):
            h.append(lista[i])
    print(h)
    print('i) afişează pe ecran poziţiile (indicii) componentelor impare negative:')
    impare_negative=[]
    for i in range(0,len(lista)):
        if (lista[i]%2 != 0) and (lista[i]<0):
            impare_negative.append(i)
    print(impare_negative)
    print('k) înlocuieşte prima componentă a tabloului cu componenta de valoare minimă din tabloul respectiv:')
    t=lista[:]
    t[0]=min(t)
    print(t)
    print('l) înlocuieşte componenta de valoare minimă din tabloul respectiv cu prima componentă a acestuia:')
    t1=lista[:]
    t1[t1.index(min(t1))] = t1[0]
    print(t1)
    print('m) creează un tablou nou, format doar din componentele pare ale tabloului introdus de la tastatură:', d)
    print('n) creează un tablou nou, format doar din componentele divizibile cu 3 ale tabloului introdus de la tastatură:')
    t2=[]
    for i in range(0,len(lista)):
        if lista[i]%3==0:
            t2.append(lista[i])
    print(t2)
else:
    print('Eroare')
