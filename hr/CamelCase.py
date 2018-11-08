import re
# Complete the camelcase function below.
def camelcase(s):
    if len(s) == 0:
        return 0
    if s[0].isupper():
        return 0
    words = re.split("[A-Z]",s)
    return len(words)

if __name__ == '__main__':
    s = ""

    result = camelcase(s)

    # print(result)