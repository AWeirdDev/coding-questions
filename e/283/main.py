import sys

MAPPING = {5: "A", 7: "B", 2: "C", 13: "D", 8: "E", 12: "F"}


def read() -> str:
    ln = sys.stdin.readline().rstrip()
    if not ln:
        exit()
    return ln


while True:
    lines = int(read())
    result = ""
    for _ in range(lines):
        result += MAPPING[int(read().replace(" ", ""), 2)]

    print(result)
