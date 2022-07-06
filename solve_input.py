from cal_24 import cal_24
def convert(s: str):
    if s.lower() == 'j':
        return 11
    elif s.lower() =='q':
        return 12
    elif s.lower() =='k':
        return 13
    elif s.lower() == 'a':
        return 1
    return int(s)

while True:
    a,b,c,d = map(convert, input("please input your 4 number: ").split(' '))
    list(map(print,cal_24(a,b,c,d)))