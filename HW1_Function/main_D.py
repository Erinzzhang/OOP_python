# main_D.py

import dice, coin, game

# data
myID = 15 % 3
k = 3

N = 3
pt = myID + 1
dice_prob = 0.15
coin_prob = 0.4

coin_num = coin.coin(coin_prob)

times = 0

# Who wins?
while times < k: 
    times += 1
    print(str(times) + ". ")
    pc = dice.sum(pt, dice_prob, k)
    player = dice.sum(pt, dice_prob, k)

    if game.show(pc,player,coin_num):
        break
    
    