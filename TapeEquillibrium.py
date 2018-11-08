# def solution(A):
#     # write your code in Python 3.6
#     #choose pivot
#     l = len(A)
#     minDiff = 2000
#     pivot = 1
#     while pivot < l:
#
#         i = pivot
#         j = 0
#         result1 = 0
#         result2 = 0
#         diff = 0
#         while i < l:
#             result1 = result1 + A[i]
#             i = i + 1
#         while j < pivot:
#             result2 = result2 + A[j]
#             j = j + 1
#
#         diff = abs(result1 - result2)
#         if diff < minDiff:
#             minDiff = diff
#
#         pivot = pivot + 1
#     return minDiff
#

import sys


def solution(A):
    # 1st pass
    parts = [0] * len(A)
    parts[0] = A[0]

    for idx in range(1, len(A)):
        parts[idx] = A[idx] + parts[idx - 1]

    # 2nd pass
    solution = sys.maxsize
    for idx in range(0, len(parts) - 1):
        solution = min(solution, abs(parts[-1] - 2 * parts[idx]));

    return solution

if __name__ == "__main__":
    A=[0]*5
    A[0] = 3
    A[1] = 1
    A[2] = 2
    A[3] = 4
    A[4] = 3
    print(solution(A))
