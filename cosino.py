import random

roney_user = 1000
roney_cosino = 1000
while roney_user and roney_cosino:
    user_turn = random.randint(1, 6)
    casino_turn = random.randint(1, 6)

    print("У игрока", roney_user, "монет")
    print("У казино", roney_cosino, "монет")
    input("Нажмите ENTER чтобы сделать ход")

    print("Игрок выбросил", user_turn)
    print("Казино выбросил", casino_turn)

    if casino_turn > user_turn:
        print("Казино победил")
        roney_user -= 100
        roney_cosino += 100
    elif casino_turn < user_turn:
        print("Игрок победил")
        roney_user += 100
        roney_cosino -= 100
    else:
        print("Ничья")


