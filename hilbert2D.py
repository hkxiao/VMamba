def hilbert_curve(n, x, y):
    if n == 0:
        return 1
    m = 1 << (n - 1)
    if x <= m and y <= m:
        return hilbert_curve(n - 1, y, x)
    if x > m and y <= m:
        return 3 * m * m + hilbert_curve(n - 1, m - y + 1, 2 * m - x + 1)
    if x <= m and y > m:
        return m * m + hilbert_curve(n - 1, x, y - m)
    if x > m and y > m:
        return 2 * m * m + hilbert_curve(n - 1, x - m, y - m)


for n in range(1,7):
    reverse_map = [1] * (1<<(n*2))

    with open('hilbert2d_'+str(n)+'.txt', 'w') as f:
        for x in range(1, (1<<n) + 1):
            for y in range(1, (1<<n) + 1):
                rank = hilbert_curve(n, x, y) - 1
                print(rank, end=" ")
                f.write(str(rank) + ' ')
                reverse_map[rank] = x - 1 + (y - 1) * (1<<n)
            print('\n')
    with open('hilbert2d_'+str(n)+'_reverse.txt', 'w') as f:
        for x in reverse_map:
            f.write(str(x) + ' ') 
    f.close()