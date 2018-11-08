def solution(A):
    # write your code in Python 3.6
    b = {}
    for i in A:
        if i in b:
            del(b[i])
        else:
            b[i] = 1
    for i in b.keys():
        return i

if __name__ == "__main__":
    solution([1, 2, 1])

