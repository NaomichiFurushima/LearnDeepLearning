from operator import add
def AND (signal, bias, theta = 0):
    t = bias + reduce(add, map(lambda xw : xw[0] * xw[1], signal))
    if t <= 0:
        return 0
    else:
        return 1
