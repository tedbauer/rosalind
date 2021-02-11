s = input()
t = input()

hamming_distance = 0
for i in range(len(s)):
    if s[i] != t[i]:
        hamming_distance += 1

print(hamming_distance)

