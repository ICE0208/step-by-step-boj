h, m = map(int, input().split())

times = 60 * h + m
early_times = times - 45

if early_times < 0:
    early_times = 60 * 24 + early_times

print(early_times // 60, early_times % 60)
