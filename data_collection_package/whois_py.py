from collections import defaultdict


def add_num(a):
    a[1] = 10
    a[2] = 10
    return a

def add_num_plus(a):
    a[3] = 12
    a[4] = 13
    return a

if __name__ == '__main__':
    a = defaultdict()
    m = a.copy()
    b = add_num(a)
    c = add_num_plus(m)
    print b, c
