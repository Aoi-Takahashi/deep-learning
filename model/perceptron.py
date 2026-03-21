def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    y = w1 * x1 + w2 * x2
    if y <= theta:
        print(f"Not Fire y is {y}")
        return 0
    else:
        print(f"Fire! y is {y}")
        return 1
