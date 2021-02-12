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

res = perms(set([i for i in range(1, n+1)]))
print(len(res))
for perm in res:
    print (" ".join(list(map(lambda x: str(x), perm))))
