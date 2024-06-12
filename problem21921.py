N, X = map(int, input().split())
arr = list(map(int, input().split()))

maxi, cnt = sum(arr[:X]), 1
temp = maxi

for i in range(X, N):
    temp = temp + arr[i] - arr[i - X]
    if maxi < temp:
        maxi = temp
        cnt = 1
    elif maxi == temp:
        cnt += 1

if maxi:
    print(maxi)
    print(cnt)
else:
    print("SAD")