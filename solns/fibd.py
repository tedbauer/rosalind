inp = input().split(" ")
n, m = int(inp[0]), int(inp[1])

babies = [1]
new_adults = [0]
old_adults = [0]
for i in range(1, n):
    babies.append(new_adults[i-1] + old_adults[i-1])
    new_adults.append(babies[i-1])

    old_adults.append(new_adults[i-1] + old_adults[i-1])
    if i-m >= 0:
        old_adults[i] -= babies[i-m]

print(babies[i] + new_adults[i] + old_adults[i])
