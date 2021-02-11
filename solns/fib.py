inp = input().split(" ")
n, k = int(inp[0]), int(inp[1])

res = [1, 1]
for i in range(2, n):
    res.append(res[i-1] + k * res[i-2])

print(res[n-1])
