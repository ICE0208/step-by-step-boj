h, m = map(int, input().split())
time = int(input())

answer_time = (h * 60 + m + time) % (60 * 24)
answer_h = answer_time // 60
answer_m = answer_time % 60
print(answer_h, answer_m)
