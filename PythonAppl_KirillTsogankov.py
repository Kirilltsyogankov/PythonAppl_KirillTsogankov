from math import * #поменял фром и импорт местами
print("Ruudu karakteristikud")
a=float(input("Sisesta ruudu külje pikkus => "))#добавил ""
S=a**2
print("Ruudu pindala", S)
P=4*a
print("Ruudu ümbermõõt", P)
di=a*sqrt(2)
print("Ruudu diagonaal", round(di,2))
print()
print("Ristküliku karakteristikud")
b=float(input("Sisesta ristküliku 1. külje pikkus => "))
c=float(input("Sisesta ristküliku 2. külje pikkus => "))
S=b*c
print("Ristküliku pindala", S)
P=2*(b+c)
print("Ristküliku ümbermõõt", P)
di=sqrt(b**2+c**2)
print("Ristküliku diagonaal", round(di)) #добавил скобки
print()
print("Ringi karakteristikud")
r=float(input("Sisesta ringi raadiusi pikkus => "))
d=2*r      #поставил R в скобки
print("Ringi läbimõõt"+ str(d))   #добавил скобки
S=pi*r**2
print("Ringi pindala", round(S))
C=2*pi*r   #поставил PI в скобки
print("Ringjoone pikkus", round(C))     #добавил скобки
