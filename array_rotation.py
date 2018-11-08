def solution(A, K):
    # write your code in Python 3.6
    l = len(A)
    if l == 0 or l == 1:
        return A
    B = [0]*l
    index = 0
    for i in A:

        newindex = (K % l) + index

        if newindex < l:
            B[newindex] = A[index]
        else:
            B[newindex - l] = A[index]
        index = index + 1
    return B
if __name__ == "__main__":
    print(solution([1,2,3,4,5], 8))


