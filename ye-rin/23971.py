H, W, N, M = map(int, input().split())

vertical_seats = (H - 1) // (N + 1) + 1
horizontal_seats = (W - 1) // (M + 1) + 1

total_seats = vertical_seats * horizontal_seats

print(total_seats)