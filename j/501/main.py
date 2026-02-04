# optimal optimistic optimization

import sys
from collections import deque


def run(n: int):
    plates: deque[int] = deque()
    orders: dict[int, deque[int]] = {}

    def check():
        result = ""
        while plates:
            first = plates.popleft()
            result += f"{orders[first].popleft()} "

        return result.rstrip()

    for i in range(n):
        plate, order = map(int, sys.stdin.readline().split())

        plates.append(plate)
        if order not in orders:
            orders[order] = deque()

        orders[order].append(i + 1)

    sys.stdout.write(check() + "\n")


try:
    while True:
        run(int(sys.stdin.readline()))
except (EOFError, ValueError):
    exit()
