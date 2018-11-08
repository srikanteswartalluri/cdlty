
def solution(S, P, Q):
    codes = {"A": 1,
             "C": 2,
             "G": 3,
             "T": 4}
    result = []
    for i in range(len(P)):
        l = S[P[i]:Q[i] + 1]
        min = codes[l[0]]
        for k in l:
            if codes[k] < min:
                min = codes[k]
        result.append(min)
    return result


if __name__ == "__main__":

    S = "CAGCCTA"
    P = [2, 5, 0]
    Q = [4, 5, 6]



    print(solution(S, P, Q))