n = int(input())

def perms(nums):
    if len(nums) == 0:
        return [[]]
    elif len(nums) == 1:
        return [list(nums)]
    else:
        res = []
        for elem in nums:
            perms2 = perms(nums.difference({elem}))
            for p in perms2:
                res.append([elem] + p)
        return res


positives = set([i for i in range(1, n+1)])
negatives = set([i for i in range(-1, -(n+1), -1)])
res = perms(positives.union(negatives))
print(len(res))
for perm in res:
    print (" ".join(list(map(lambda x: str(x), perm))))
