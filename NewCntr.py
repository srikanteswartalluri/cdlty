def solution(N, A):
    # write your code in Python 3.6
    cntrs = [0]*N
    for j in A:
        if j <= N:
            cntrs[j-1] = cntrs[j-1] + 1
        elif j == N + 1:
            temp = max(cntrs)
            cntrs = [temp]*N
    return cntrs




if __name__ == "__main__":
    A = [0] * 3
    A[0] = 1
    A[1] = 1
    A[2] = 1
    # A[3] = 6
    # A[4] = 1
    # A[5] = 4
    # A[6] = 4
    print(solution(1, A))
