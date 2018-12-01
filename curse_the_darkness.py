def in_circle(center_x, center_y, x, y, radius):
    return (center_x - x) ** 2 + (center_y - y) ** 2 <= radius ** 2

m = int(input())

for i in range(m):
    book_x, book_y = map(float, input().split())
    n = int(input())
    done = False
    for j in range(n):
        x, y = map(float, input().split())
        if not done and in_circle(book_x, book_y, x, y, 8):
            print('light a candle')
            done = True
    if not done:
        print('curse the darkness')
