def solution(A):
    # write your code in Python 3.6
    a = set(A)
    for i in range(1, len(A)+1):
        if i not in a:
            return i
    return A[len(A)-1] + 1



if __name__ == "__main__":
    print(solution([1,2,3,6]))