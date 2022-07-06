from math import nan, comb
from random import shuffle
from fractions import Fraction
from itertools import combinations, permutations, product
from datetime import datetime
# import matplotlib.pyplot as plt
from collections import deque, Counter

all_op = [Fraction.__add__, Fraction.__sub__,
          Fraction.__mul__, Fraction.__truediv__,
          Fraction.__rsub__, Fraction.__rtruediv__]

all_op_str = ['+','-','*','/','r-','r/']

all_op_dict = {all_op[i]: all_op_str[i] for i in range(len(all_op))}

def get_card_comb_prob(a,b,c,d):
    res = Fraction(1, comb(13*4, 4))
    cur_card_cum = Counter((a,b,c,d))
    for card in cur_card_cum:
        res *= comb(4,cur_card_cum[card])
    return res

def tree1(a,b,c,d,op1,op2,op3):
    try:
        return op3(op1(a,b),op2(c,d))
    except Exception as e:
        return nan

def get_expr_str(a,b,op):
    global all_op_dict
    if all_op_dict[op] in ['r-', 'r/']:
        return '('+b + all_op_dict[op][-1] + a +')'
    return '('+a + all_op_dict[op] + b+')'

def tree1_str(a, b, c, d, op1, op2, op3):
    a,b,c,d = str(a),str(b),str(c),str(d)
    return get_expr_str(get_expr_str(a, b, op1), get_expr_str(c, d, op2), op3)

def tree2(a,b,c,d,op1,op2,op3):
    try:
        return op3(op2(op1(a,b),c),d)
    except Exception as e:
        return nan

def tree2_str(a, b, c, d, op1, op2, op3):
    a, b, c, d = str(a), str(b), str(c), str(d)
    return get_expr_str(get_expr_str(get_expr_str(a, b, op1), c, op2), d, op3)

def cal_24(i,j,k,l):
    global all_op
    cnt = 0
    res_set=set()
    for a, b, c, d in permutations([i, j, k, l]):
        # print(f"currnet a b c d {a,b,c,d}")
        for op1, op2, op3 in product(all_op,all_op,all_op):
            res1 = tree1(a,b,c,d,op1,op2,op3)
            res2 = tree2(a,b,c,d,op1,op2,op3)
            # print(f"{tree1_str(a,b,c,d,op1,op2,op3)}={res1}")
            # print(f"{tree2_str(a,b,c,d,op1,op2,op3)}={res2}")
            if res1 ==24:
                res_set.add(f"{tree1_str(a,b,c,d,op1,op2,op3)}={res1}")
            if res2 == 24:
                res_set.add(f"{tree2_str(a,b,c,d,op1,op2,op3)}={res2}")
            cnt +=2
    # print(f"total cal cnt:{cnt}")
    return res_set




