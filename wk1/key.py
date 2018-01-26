def roots(a, b, c):
    disc = b ** 2 - 4 * a * c
    if(disc < 0): return None
    elif(disc == 0): return - b / (2 * a)
    else:
        r1 = (- b + Math.sqrt(disc)) / (2 * a)
        r2 = (- b - Math.sqrt(disc)) / (2 * a)
        return r1, r2

