def solution(A):
    # write your code in Python 3.6
    # n = len(A)
    # p = []
    # k = 1
    # p = [0] * (n + 1)
    #
    # for k in range(1, n+1):
    #     p[k] = p[k-1] + A[k - 1]


    # print(p)
    # result = []
    # n = len(A)
    # for k in range(n):
    #     if A[k] == 0:
    #         for j in range(k+1, n):
    #             if A[j] == 1:
    #                 result.append((k,j))
    #             if len(result) > 1000000000:
    #                 return -1
    #     else:
    #         continue
    #
    # return len(result)
    west = 0
    passing =0
    for index in range(len(A)-1, -1, -1):
        if A[index] == 0: #east going
            passing = passing + west
            if passing == 1000000000:
                return -1
        else:
            west = west + 1
    return passing




if __name__ == "__main__":
    A = [0]*5#[1, 2, 3, 4, 5]
    A[0] = 0
    A[1] = 1
    A[2] = 0
    A[3] = 1
    A[4] = 1
    print(solution(A))