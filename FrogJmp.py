def solution(X, Y, D):
    # write your code in Python 3.6
    if X == Y:
        return 0
    hops = 0
    minHops = (Y-X) // D
    if (Y-X) % D == 0:
        hops = minHops
    else:
        hops = minHops + 1
    return hops



if __name__ == "__main__":
    print(solution(4, 5, 1))