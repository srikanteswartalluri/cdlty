def solution(X, A):
    # write your code in Python 3.6
    b = {}
    for i in range(1, X+1):
        b[i] = 0
    index = 0
    for j in A:
        if j in b:
            del b[j]
        if len(b) == 0:
            return index
        index = index + 1
    return -1






if __name__ == "__main__":
    A = []#[0]*1
   # A[0] = 1
    # A[1] = 3
    # A[2] = 1
    # A[3] = 4
    # A[4] = 2
    # A[5] = 3
    # A[6] = 5
    # A[7] = 4
    print(solution(5, A))
