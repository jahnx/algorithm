n, k = list(map(int, input().split()))

# 첫번째 풀이
arr = []

for i in range (1, n + 1):
    if (n % i == 0) :
        arr.append(i)

if (len(arr) < k):
    print(0)
else:
    print(arr[k-1])
    
# 두번째 풀이
cnt = 0

for i in range(1, n + 1):
    if n % i == 0:
        cnt += 1
    if cnt == k:
        print(i)
        break
else:
    print(0)
