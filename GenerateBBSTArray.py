def GenerateBBSTArray(a):
    balans_massiv = [None] * 3
    a = sorted(a)
    ind = 1

    def binary_sort(a, s_m, x):
        if not a:
            return None
        if x >= len(s_m):
            nonlocal ind
            ind += 1
            l1 = 2 ** (ind + 1) - 1
            s_m += ([None] * (l1 - len(s_m)))
        centr = int(len(a)/2)
        s_m[x] = a[centr]
        binary_sort(a[:centr], s_m, x * 2 + 1)
        binary_sort(a[centr+1:], s_m, x * 2 + 2)
        return s_m

    balans_massiv = binary_sort(a, balans_massiv, 0)
    return balans_massiv