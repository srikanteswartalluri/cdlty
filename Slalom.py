def solution(A):
    counter = 0
    count = 0
    newList = []
    dir = "left"
    dirChange = 0
    for i in A:
        # print("{}{}".format(" "*(i-1), "*"))
        if counter+1 == len(A):
            break
        #move left
        newList.append(i)
        if A[counter] > A[counter+1]:
            if dir == "left":
                dirChange += 1
                dir = "right"
            else:
                pass
        else:
            if dir == "right":
                dirChange += 1
                dir = "left"
            else:
                pass
        counter += 1
    return count



if __name__ == "__main__":
    A = [0]*13
    A[0] = 15
    A[1] = 13
    A[2] = 5
    A[3] = 7
    A[4] = 4
    A[5] = 10
    A[6] = 12
    A[7] = 8
    A[8] = 2
    A[9] = 11
    A[10] = 6
    A[11] = 9
    A[12] = 3
    print(solution(A))