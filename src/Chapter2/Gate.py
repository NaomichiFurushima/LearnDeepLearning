from operator import add
def AND(signal):
    w = 0.5
    b = -0.7
    theta = 0 
    d = map(lambda x: (x, w), signal)
    t = b + reduce(add, map(lambda x: x[0] * x[1], d))
    if t <= theta:
        return 0
    else:
        return 1
