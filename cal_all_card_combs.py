from collections import deque
from datetime import datetime
from itertools import combinations
from random import shuffle

from cal_24 import cal_24, get_card_comb_prob


def card_generator():
    for i in range(1,14):
        for j in range(i,14):
            for k in range(j,14):
                for m in range(k,14):
                    yield (i,j,k,m)
                    
if __name__ == "__main__":
    total_prob = 0
    ok_prob = 0

    all_cards = [i for i in range(1, 14) for j in range(4)]
    all_comb = list(card_generator())
    # all_comb = list(combinations(all_cards, 4))
    shuffle(all_comb)
    # comb_num = len(all_comb)  # comb(52,4)
    x, y = [], []
    last_100 = deque([], maxlen=100)
    get_last_100_prob = lambda : sum(map(lambda x:x[0], filter(lambda x: x[1], last_100)))/sum(map(lambda x:x[0], last_100))
    start_time = datetime.now()

    for i, (a, b, c, d) in enumerate(all_comb):
        res = cal_24(a, b, c, d)
        cur_prob = get_card_comb_prob(a,b,c,d)
        total_prob += cur_prob
        if len(res) > 0:
            ok_prob += cur_prob
            last_100.append((cur_prob,True))
        else:
            last_100.append((cur_prob,False))
        
        if i%10 == 0:
            print(f"progress: {i}/{len(all_comb)}, OK ration: {ok_prob/total_prob}={float(ok_prob/total_prob):.3f}, last 100 ratio: {get_last_100_prob()}={float(get_last_100_prob()):.2f}, ", end='')
            print(f"current a,b,c,d: {a,b,c,d}, shown prob: {cur_prob}", end=', ')
            print(next(iter(res)) if len(res) > 0 else "No solution")
        x.append(ok_prob/total_prob)
        y.append(total_prob)

    end_time = datetime.now()
    print(f"OK ration: {ok_prob}={float(ok_prob)}")
    print(f"used time: {end_time-start_time}")
    # plt.plot(x,y)
    # plt.show()
