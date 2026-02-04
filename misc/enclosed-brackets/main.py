import sys

PAIRING = {"(": 1, "[": 2, "{": 3, ")": -1, "]": -2, "}": -3}


def is_valid(text: str):
    stack = []

    for ch in text:
        representation = PAIRING[ch]

        if representation > 0:
            stack.append(representation)
        else:
            if not stack:
                return False

            if representation + stack.pop():
                return False

    return not stack


try:
    while True:
        input_ = sys.stdin.readline().rstrip()
        if not input_:
            break

        print(is_valid(input_))
except EOFError:
    exit()
