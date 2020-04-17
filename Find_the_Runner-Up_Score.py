n = int(input())
arr = list(map(int, input().split()))
m = max(arr)

for i in range(n):
    if m == max(arr):
        arr.remove(max(arr))

print(max(arr))
