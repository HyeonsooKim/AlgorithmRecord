import sys
n = int(sys.stdin.readline().rstrip())
control_list = list(sys.stdin.readline().rstrip().split())

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
d = ['L', 'U', 'R', 'D']
pos = [1, 1]
temp = 0

for i in control_list:
    temp = pos[0]
    pos[0] += dy[d.index(i)]
    if pos[0] < 1 or pos[0] > n:
        pos[0] = temp

    temp = pos[1]
    pos[1] += dx[d.index(i)]
    if pos[1] < 1 or pos[1] > n:
        pos[1] = temp

print(*pos)



# 제시 풀이법
# N 입력받기
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인하기
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)