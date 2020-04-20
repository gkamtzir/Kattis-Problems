m = int(input())

while m != 0:
    final_width = 0
    final_height = 0
    row_width = 0
    row_height = 0
    width, height = map(int, input().split())
    while width != -1 and height != -1:
        if row_width + width <= m:
            row_width += width
            if height > row_height:
                row_height = height
        else:
            if row_width > final_width:
                final_width = row_width
            final_height += row_height
            row_height = 0
            row_width = 0
            if row_width + width <= m:
                row_width += width
                row_height = height
        width, height = map(int, input().split())
    final_height += row_height
    if row_width > final_width:
        final_width = row_width
    print(f"{final_width} x {final_height}")
    m = int(input())
