A = 55

lesson = int(input("Введите номер урока, время которого вы хотите узнать "))

if lesson == 1:
    Cl = 510 + (A - 10)

else:
    Cl = 510 + ((lesson * A) - 10)

Cl1 = Cl

Cl2 = Cl

Cl1 //= 60

Cl2 %= 60

while Cl1 > 23:
    if Cl1 > 23:
        Cl1 -= 24


if Cl2 >= 10:
    print(f"{Cl1}:{Cl2}")
else:
    print(f"{Cl1}:0{Cl2}")