import os
from random import randint
money = 0
int(money)
at = 0
int(at)
name = input("Введите имя героя ")
pl_name = name
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
            dont_agree = input('Девушка предлагает перес@@@@, 1 - Согласился, 2 - Отказать')
            if dont_agree == "1":
                print(f"Княжна заманила вас в комнату.(НА СЛЕДУЮЩИЕ УТРО) княжна придложила обручиться и {name} согласился, но с каждым днем жизни вы чувствовали себя хуже и хуже пока одним вечером не узнали что княжна травит вас чтобы после вашей смерти получить богатство {name}.Плохая концовка :(")
                break
            elif dont_agree == "2":
                print(f"Вы сказали кнежне что скоро прийдете, но на самом деле {name} пытается выбраться через туалет и случайно дергает за рычаг открываеться тойнвй проход и {name} по тунелю выбираеться к камню")
                way_center = True
            else:
                print("Такого выбора не предусматривалось возможно в будующем это исправят, ХОТЯ МЫ ОБА ЗНАЕМ ЧТО ТЫ ПРОСТО ГРЯЗНЫЙ ХАКЕР")
                print("YOU DEAD YOU DEAD YOU DEAD YOU DEAD YOU DEAD YOU DEAD YOU DEAD YOU DEAD YOU DEAD АХАХАХАХАХАХАХАХАХАХАХАХАХАХАХ ИГРАЙ СНАЧАЛА")
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
                print(f"{name} поехал дальше и нашел пещеру с богатствами, он забрал их себе и поехал в придорожную лавку")
                money += 1000
                way_left = True
                print(f"В лавке вас ожидал продавец и он спросил вас хотите ли вы купить кибер броню и кибер меч за 1000 монет. У вас {money} денег")
                if money >= 1000:
                    print("Поздравляю вы приобрели кибер броню и кибер меч за 1000 монет вы отправляетесь дальше")
                    at += 10
                elif money < 1000:
                    print("У вас нехватило денег и вы поехали дальше")
            else:
                print("Такого выбора не предусматривалось возможно в будующем это исправят, ХОТЯ МЫ ОБА ЗНАЕМ ЧТО ТЫ ПРОСТО ГРЯЗНЫЙ ХАКЕР")
                print("YOU DEAD YOU DEAD YOU DEAD YOU DEAD YOU DEAD YOU DEAD YOU DEAD YOU DEAD YOU DEAD АХАХАХАХАХАХАХАХАХАХАХАХАХАХАХ ИГРАЙ СНАЧАЛА")
                break
        else:
            print("Вы уже были на этой дороге")
    else:
        os.system('cls')
        print(f"{name} хочет выйти из игры. ЧТО? ГРЯЗНЫЙ ХАКЕР ТЫ ДУМАЕШЬ ЧТО МОЖЕШЬ ТАК ПРОСТО ПОКИНУТЬ ЭТО МЕСТО АХАХАХАХАХАХАХАХАХАХАХАХАХАХАХ")
        print("ПРАВИЛЬНЫЙ ОТВЕТ НЕТ НЕТ НЕТ НЕТ НЕТ НЕТ НЕТ")
print("Конец:)")