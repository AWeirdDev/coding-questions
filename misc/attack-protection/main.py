lines = int(input())
characters = []

for i in range(lines):
    attack, protect = map(int, input().split())
    characters.append((i, attack**2 + protect**2, attack, protect))

item = sorted(characters, key=lambda i: i[1], reverse=True)[1]
print(item[2], item[3])
