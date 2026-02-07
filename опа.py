f1 = [0, 8, 9, 7, 6, 10, 5]
f2 = [0, 6, 7, 5, 9, 8, 10]
f3 = [0, 10, 4, 8, 7, 6, 9]
f4 = [0, 9, 8, 6, 5, 7, 6]
f5 = [0, 7, 6, 9, 8, 5, 7]
f6 = [0, 12, 9, 10, 6, 9, 8]
fs = [f1, f2, f3, f4, f5, f6]

S = 6
n = 6

w = [[0]*(S+1) for _ in range(n+1)]
xopt = [[0]*(S+1) for _ in range(n+1)]

for k in range(1, n+1):
    f = fs[k-1]
    for C in range(S+1):
        best = -10**9
        best_x = 0
        for x in range(C+1):
            val = f[x] + w[k-1][C-x]
            if val > best:
                best, best_x = val, x
        w[k][C] = best
        xopt[k][C] = best_x

print("Максимальный эффект:", w[n][S])

C = S
xs = [0]*n
for k in range(n, 0, -1):
    xs[k-1] = xopt[k][C]
    C -= xs[k-1]

print("Оптимальное распределение:", xs)