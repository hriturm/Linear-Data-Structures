def TOH(n, start, end, aux):
    if n == 0:
        return
    TOH(n - 1, start, aux, end)
    print("Move disk", n, "from rod", start, "to rod", end)
    TOH(n - 1, aux, end, start)

n = 3
TOH(n, 'A', 'C', 'B')