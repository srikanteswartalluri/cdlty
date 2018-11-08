def solution(A):
    # write your code in Python 3.6
    if len(A) == 1 and A[0] == 1:
        return 1
    A.sort()
    #print(A)
    count = 1
    for i in A:
        if count != i:
            return 0
        count = count + 1
    return 1


if __name__ == "__main__":
    print(solution([1, 2]))

