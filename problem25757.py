N, Type = input().split()

people = set()
for _ in range(int(N)):
    people.add(input().strip())

dic = {
    "Y" : 1,
    "F" : 2,
    "O" : 3,
}

print(len(people) // dic[Type])