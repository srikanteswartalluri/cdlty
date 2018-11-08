import re
numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"


def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    req = 0
    oldreq = 0
    if len(password) < 6:
        oldreq = 6 - len(password)
    else:
        pass

    #find strength
    #uppercase
    match = re.findall("[A-Z]", password)
    if len(match) == 0:
        req += 1
        print("upp")
    #lowercase
    match = re.findall("[a-z]", password)
    if len(match) == 0:
        req += 1
        print("low")
    #number
    match = re.findall("[0-9]", password)
    if len(match) == 0:
        req += 1
        print("num")
    #special char
    match = re.findall("[!@#$%^&*()\-+]", password)
    if len(match) == 0:
        req += 1
        print("sp")


    if oldreq >= req:
        return oldreq
    else:
        return req


if __name__ == '__main__':
    password = "4700"
    n = len(password)

    answer = minimumNumber(n, password)
    print(answer)

