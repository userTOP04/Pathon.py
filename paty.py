s = int(input("Введите количество секунд "))

h = s // 3600

s = s % 3600

m = s // 60

s = s % 60

print(f"{h} ч. {m} м. {s} с.")