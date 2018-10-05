# main_A_1.py

import dice, coin, game

# data
myID = 15 % 3
k = myID *2 + 3

N = 2
pt = myID + 1
dice_prob = 0.15
coin_prob = 0.5

coin_num = coin.coin(coin_prob)

times = 0

# Who wins?
while times < k: 
    times += 1
    print(str(times) + ". ")
    pc = dice.multi_dice(N, pt, dice_prob, myID)
    player = dice.multi_dice(N, pt, dice_prob, myID)
    if game.show(pc,player,coin_num):
        break

    