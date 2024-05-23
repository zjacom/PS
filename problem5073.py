result = []

while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break

    maxi = max(a, b, c)
    if 2 * maxi >= a + b + c:
        result.append("Invalid")
    elif a == b == c:
        result.append("Equilateral")
    elif a == b or a == c or b == c:
        result.append("Isosceles")
    elif a != b != c:
        result.append("Scalene")

for res in result:
    print(res)