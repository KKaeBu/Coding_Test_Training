n = int(input())

# 1분(0~59초 동안 3의 등장 횟수 세기)
ts_count = len([i for i in range(60) if i % 10 == 3 or i // 10 == 3])

# 60분(0~59분 동안 3의 등장 횟수 세기)
# 0~2 & 4~9 -> 총 9번 * ts_count, 3분대 -> 60번, 30분대 -> 10 * 60
# 0분대&10분,20분,40분,50분대 = 5*(총 9번 * ts_count), 30분대 -> 10 * 60
tm_count = 5 * (9 * ts_count + 60) + (10 * 60)

# 시간 기준으로 3의 등장 횟수
# 3시, 13시, 23시 -> 60분 내내 등장 -> 60 * 60 = 3600
# 나머지 시간대 -> 0~2는 3 * tm_count, 4~9는 6 * tm_count
t_count = 0
for i in range(n + 1):
    if i % 10 == 3:
        t_count += 3600
    else:
        t_count += tm_count

print(t_count)
