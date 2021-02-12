inp = list(map(lambda x: int(x), input().split(" ")))
k, m, n = inp[0], inp[1], inp[2] 
total = k + m + n

# d = dominant, r = recessive
# xy = factor with allele x and allele y
# ab_cd = probability of organism with factor ab
#         crossed with organism with factor cd
dd_dd = (k / total) * ((k-1) / (total-1))
dd_dr = (k / total) * (m / (total-1))
dr_dd = (m / total) * (k / (total-1))
dd_rr = (k / total) * (n / (total-1))
rr_dd = (n / total) * (k / (total-1))
dr_rr = (m / total) * (n / (total-1))
rr_dr = (n / total) * (m / (total-1))
dr_dr = (m / total) * ((m-1) / (total-1))

ans = (dd_dd * 1) + (dd_dr * 1) + (dr_dd * 1) + \
        (dd_rr * 1) + (rr_dd * 1) + (dr_rr * (1/2)) + \
        (rr_dr * (1/2)) + (dr_dr * (3/4))

print(ans)

