# coin.py
import random
def coin(prob):
    temp = random.random()
    if prob < 0.45:
        prob = 0.45
    elif prob > 0.55:
        prob = 0.55
    else:
        prob = prob
    
    if temp <= prob:
        return 1
    else:
        return 2

