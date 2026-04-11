def cong(a, b, c, d):
    return (a*d + b*c, b*d)

def tru(a, b, c, d):
    return (a*d - b*c, b*d)

def nhan(a, b, c, d):
    return (a*c, b*d)

def chia(a, b, c, d):
    if c == 0:
        raise ValueError("Không thể chia cho 0")
    return (a*d, b*c)