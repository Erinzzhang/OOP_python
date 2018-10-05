# gmae.py
def show(pc,player,coin_num):
    if player >= pc and coin_num == 1:
        print("the head side of the coin")
        print("pc: ", pc)
        print("player: ", player)
        print("player win")
        return False
    elif player > pc and coin_num == 2:
        print("the number side of the coin")
        print("pc: ", pc)
        print("player: ", player)
        print("pc win")
        return True
    elif player < pc and coin_num == 1:
        print("the number side of the coin")
        print("pc: ", pc)
        print("player: ", player)
        print("pc win")
        return True
    elif player <= pc and coin_num == 2:
        print("the head side of the coin")
        print("pc: ", pc)
        print("player: ", player)
        print("player win")
        return False
    else:
        print("!!!!!")
        return True