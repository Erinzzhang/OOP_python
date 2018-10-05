# dice.py

import random

def dice (pt, prob):
    random_prob = random.random()
    other_prob = float((1.0-prob)/5.0)
    number = [1, 2, 3, 4, 5, 6]

    if random_prob > 0 and random_prob <= prob:
        out_pt = pt
    else:
        number.remove(pt)
        if random_prob > prob and random_prob <= prob + other_prob:
            out_pt = number[0] 
        elif random_prob > (prob + other_prob) and random_prob <= prob + other_prob * 2:
            out_pt = number[1]
        elif random_prob > prob + other_prob*2 and random_prob <= prob + other_prob * 3:
            out_pt = number[2]
        elif random_prob > prob + other_prob*3 and random_prob <= prob + other_prob * 4:
            out_pt = number[3]
        elif random_prob > prob + other_prob*4 and random_prob <= prob + other_prob * 5:
            out_pt = number[4]

    return out_pt

def multi_dice(N,pt, prob,myID):
    sum = 0
    for x in range(N):
        if x == 1:
            sum += dice(myID+1,0.15)
        else:
            sum += dice(pt, 1/6)
    return sum

def one_dice(pt, prob , N):
    N_value = []
    sum = 0
    if prob < 0.1:
        prob = 0.1
    elif prob > 0.25:
        prob = 0.25
    else:
        prob = prob

    for i in range(N):
        N_value.append(dice(pt,prob)) 
    return N_value

def two_dice(pt, prob, k):
    dice1 = one_dice(pt,prob,k)
    dice2 = one_dice(2,1/6,k)
    dices = dice1 + dice2
    print(dices)
    return dices

def sum(pt, prob, k):
    sum = 0
    for i in two_dice(pt, prob, k):
        sum += i
    return sum

