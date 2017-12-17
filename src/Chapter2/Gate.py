from operator import add
def GATE(sw, bias, theta):
    t = bias + reduce(add, map(lambda x: x[0] * x[1], sw))
    if t <= theta:
        return 0
    else:
        return 1

def AND(signal):
    return GATE(map(lambda x: (x, 0.5), signal), -0.7, 0)

def OR(signal):
    return GATE(map(lambda x: (x, 0.5), signal), -0.2, 0)

def NAND(signal):
    return GATE(map(lambda x: (x, -0.5), signal), 0.7, 0)
