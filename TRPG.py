import os
import random
money = 100
int(money)
at = 0
int(at)
pl_name = input("Введите имя героя ")
xp_pl = 0
pl_level = 0
hp_pl = 100 * pl_level


en_name = "Жран Борзый"
en_level = 0
hp_en = 100 * en_level



way_left = False
way_right = False
way_center = False
while way_left == False or way_center == False or way_right == False:
    print(f"Подъезжает {name} к трем дорожкам, на перекрестке камень лежит, а на том камне написано: «Кто вправо поедет - тому убитым быть, кто влево поедет - тому богатым быть, а кто прямо поедет - тому женатым быть")
    print("1 - Поеду-ка я по той дорожке, где убитому быть. Умру в чистом поле, как славный богатырь!")
    print("2 - Ну, поеду теперь, где женатому быть!")
    print("3 - Ну, поеду теперь в дорожку, где богатому быть")
    print("4 - Поеду-ка я в трактир.")
    print("5 - Пора мне и в магазин съездить")
    way = input(f"Куда поедет {name}? ")

    if way == "1":
        if way_right == False:
            os.system('cls')
            print(f"{name} ехал по дороге и вдруг ему вдруг ему на встречу разбойники стоят, они потребовали денег но у тебя их нет, ты решил убить их!")
            if at == 10:
                while True:
                    player_attack = randint(10, 20) * pl_level
                    hp_en -= player_attack
                    print(f"{pl_name} ударил {en_name} на {player_attack} жизней")
                    print(f"У {en_name} стало {hp_en} жизней")
                    input("Для продолжения нажмите ENTER")
                    enemy_attack = randint(0, 5) * en_level
                    hp_pl -= enemy_attack
                    print(f"{en_name} ударил {pl_name} на {enemy_attack} жизней")
                    print(f"У {pl_name} стало {hp_pl} жизней")
                    input("Для продолжения нажмите ENTER")
                    if hp_pl <= 0:
                        print(f"{pl_name} погиб")
                        break
                    elif hp_en <= 0:
                        print(f"{en_name} погиб, вы победили благодоря хлоршему оружию")
                        xp_pl += (en_level * 10)
                        while xp_pl >= 10:
                            pl_level += 1
                            xp_pl -= 10
                        break
            else:
                while True:
                    player_attack = randint(0, 3) * pl_level
                    hp_en -= player_attack
                    print(f"{pl_name} ударил {en_name} на {player_attack} жизней")
                    print(f"У {en_name} стало {hp_en} жизней")
                    input("Для продолжения нажмите ENTER")
                    enemy_attack = randint(5, 10) * en_level
                    hp_pl -= enemy_attack
                    print(f"{en_name} ударил {pl_name} на {enemy_attack} жизней")
                    print(f"У {pl_name} стало {hp_pl} жизней")
                    input("Для продолжения нажмите ENTER")
                    if hp_pl <= 0:
                        print(f"{pl_name} погиб из зи отсудствия хорошего оружия")
                        break
                    elif hp_en <= 0:
                        print(f"{en_name} погиб")
                        break
                break
            way_right = True
        else:
            print("Вы уже были на этой дороге")
    elif way == "2":
        if way_center == False:
            os.system('cls')
            print(f"{name} ехал по дороге и увидел замок, там в темнице была девушка вы освободили ее!")
            print("Оказалось что эта девкшка была княжной но ее заперли в собственной темнице")
            dont_agree = input('Девушка предлагает пойти в комнату, 1 - Согласился, 2 - Отказать')
            if dont_agree == "1":
                print(f"Княжна заманила вас в комнату и убила")
                break
            elif dont_agree == "2":
                print(f"Вы сказали кнежне что скоро прийдете, но на самом деле {name} пытается выбраться через туалет и случайно дергает за рычаг открываеться тойнвй проход и {name} по тунелю выбираеться к камню")
                way_center = True
            else:
                print("Такого выбора не предусматривалось возможно в будующем это исправят, ХОТЯ МЫ ОБА ЗНАЕМ ЧТО ТЫ ПРОСТО ГРЯЗНЫЙ ХАКЕР")
                print("YOU DEAD АХА ИГРАЙ СНАЧАЛА")
                break
        else:
            print("Вы уже были на этой дороге")
    elif way == "3":
        if way_left == False:
            os.system('cls')
            print(f"{name} приехал к камню. 1 - поднять камень, 2 - оставить камень и уехать ")
            way_3 = input("Выбере ответ! ")
            if way_3 == "1":
                os.system('cls')
                print(f"{name} поднял камень и увидел сундук там была связана девушка вы развязываете ее но она была вампиром и съела вас")
                break
            elif way_3 == "2":
                os.system('cls')
                print(f"{name} поехал дальше и нашел пещеру с богатствами, он забрал их себе и поехал к камню")
                money += 1000
                way_left = True
            else:
                print("Такого выбора не предусматривалось возможно в будующем это исправят, ХОТЯ МЫ ОБА ЗНАЕМ ЧТО ТЫ ПРОСТО ГРЯЗНЫЙ ХАКЕР")
                print("YOU DEAD АХАХ ИГРАЙ СНАЧАЛА")
                break
        else:
            print("Вы уже были на этой дороге")
    elif way == "4":
        way123 = int(input("Вас приветствуют в таверне и предлагают сыграть в кости. 1 - Да отичное предложение. 2 - Нет"))
        if way123 == 1:
            while True:
                bet = int(input("Выбери ставку "))
                if bet <= 0:
                    print("Нельзя поставить такую ставку")
                    input("Нажмите ENTER для продолжения")
                    break
                if bet > money:
                    (f"У {pl_name} недстадочно денег для такой ставки")
                    input("Нажмите ENTER для продолжения")
                    break
                user_turn = random.randint(1, 6)
                casino_turn = random.randint(1, 6)

                print("Игрок выбросил", user_turn)
                print("Трактирщик выбросил", casino_turn)

                if casino_turn > user_turn:
                    print("Трактирщик победил")
                    money -= 100
                    print(f"У {pl_name} {money} монет")
                elif casino_turn < user_turn:
                    print("Игрок победил")
                    roney_user += 100
                    print(f"У {pl_name} {money} монет")
                else:
                    print("Ничья")
                    print(f"У {pl_name} {money} монет")
                breakk = int(input(f"{pl_name} хотите выйти. 1 - Да, 2 - Нет"))
                if breakk == 1:
                    break
                elif breakk == 2:
                    pass
    elif way == "5":
        print(f"Торговец приветствует {pl_name} он хочет предложтьсвои товары")
        print("1 - Зелье здоровья, стоимость 100 монет, лечит 60 hp")
        print("2 - Большое зелье здоровья, стоимость 300 монет, лечит полное hp")
        print("3 - Кибер меч, стоимость 1000 монет, увеличивает силу вашего удара и уменьшает силу удара врага")
    else:
        os.system('cls')
        print(f"{name} такого выюора нет")
print("Конец:)")