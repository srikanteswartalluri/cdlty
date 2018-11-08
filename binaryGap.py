
def solution(N):
    # write your code in Python 3.6
    b = []
    while N != 0:
        b.append(N % 2)
        N = N // 2
    b.reverse()
    # print(b)
    gap = 0
    maxgap = 0
    for i in b:
        if i == 0:
            gap = gap + 1
        else:
            if maxgap < gap:
                maxgap = gap
            gap = 0
    return maxgap



if __name__ == "__main__":
    print(solution(529))
