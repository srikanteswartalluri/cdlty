def solution(A):
    # write your code in Python 3.6
    l = len(A) + 1
    result = 0
    for i in A:
        result = result + i
    print(result)
    print((l*(l+1))/2)
    return  int((l*(l+1))/2) - result

if __name__ == "__main__":
    print(solution([2, 3, 1, 5]))