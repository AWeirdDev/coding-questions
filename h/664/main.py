lines = int(input())

for _ in range(lines):
    _, steps = map(int, input().split())
    for idx, ch in enumerate(bin(steps)[2:][::-1]):
        if ch == "1":
            print(idx + 1)
            break
