A = 55
int(A)

N = "0"

lesson = int(input("Введите номер урока, время которого вы хотите узнать "))

if lesson == 1:
    Cl = 510 + (A - 10)
else:
    Cl = 510 + ((lesson * A) - 10)

Cl1 = Cl
int(Cl1)

Cl2 = Cl
int(Cl2)

Cl1 //= 60

Cl2 %= 60


print(f"{Cl1}:{Cl2}")


