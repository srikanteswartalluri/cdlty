def solution(A):
    # write your code in Python 3.6
    n = len(A)
    p = [0]* (len(A)+1)
    p[0] = 0
    q = [0] * (n+1)
    q[n] = 0
    for i in range(1, len(A)+1):
        p[i] = p[i-1] + A[i-1]

    for i in range(n - 1, -1, -1):
        q[i] = q[i+1] + A[i]

    # print("   {}".format(A))
    # print(p)
    # print("   {}".format(q))
    # total_sum  = suffix_sums(A)[0]
    # print(total_sum)
    eqs = []
    noeq = 1
    for i in range(0, n):

        if i == 0:
            left = 0
            right = q[i+1]
        elif i == n:
            right = 0
            left = p[i]
        else:
            left = p[i]
            right = q[i + 1]

        if left == right:
            eqs.append(i)
            noeq = 0

    if noeq == 1:
        return -1
    else:
        return eqs[0]




def prefix_sums(A):
    n = len(A)
    P = [0] * (n + 1)
    for k in range(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]
    return P

def suffix_sums(A):
    n = len(A)
    Q = [0] * (n + 1)
    for k in range(n-1, -1 , -1):
        Q[k] = Q[k+1] + A[k]
    return Q

if __name__ == "__main__":
    A =[0]*8
    A[0] = -1
    A[1] = 3
    A[2] = -4
    A[3] = 5
    A[4] = 1
    A[5] = -6
    A[6] = 2
    A[7] = 1
    print(solution(A))
    # print(prefix_sums(A))
    # print(suffix_sums(A))