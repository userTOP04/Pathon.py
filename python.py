import os

while True:
    os.system('cls')
    print("Тебе сниться странный сон")
    print("Выбери какую таблетку взять красную или синию таблетку")
    print("Если выберите красную то проснетесь в своей кровати и нечего не вспомните 1 - красная")
    print("Если выберете синию то узнаете правду о мире 2 - синяя")
    key = input("Выберите 1 или 2 ..........................(только не выберайте другой вариант)..............................")
    if key == "1":
        print("Ты просыпаешься в своей кровати, и вспоминаешь что тебе снился странный сон но ты его не мог вспомнить")
        print("Какой это уже раз, кажется все повторяется")
        input()
    elif key == "2":
        print("Вася Питонов смотрит этот текст в компьютернем классе, ты понимаешь что ты решил написать программу на питоне")
        print("Ты понимаешь что твоя жизнь это ложь которую ты самсебе создал, ты вподаешь в депресию и снова запускаешь программу")
        input()
    else:
        print("Почему программа слетела? Кажеться ее нужно починить...")
        break

