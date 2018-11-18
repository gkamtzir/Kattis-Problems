def wall_completable(h, w, widths):
    covered_width = 0
    j = 0
    for i in range(h):

        while covered_width < w:
            if covered_width + widths[j] <= w:
                covered_width += widths[j]
            else:
                return 'No'
            if covered_width == w and j == len(widths):
                if i == h - 1:
                    return 'Yes'
                else:
                    return 'No'
            elif j == len(widths):
                return 'No'
            j += 1
        covered_width = 0

    return 'Yes'


h, w, n = map(int, input().split())
widths = input().split()
widths = [int(x) for x in widths]

print(wall_completable(h, w, widths))
