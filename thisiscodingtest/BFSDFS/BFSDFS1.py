# 풀지 못한 문제
"""
음료수 얼려 먹기
문제
N × M 크기의 얼음 틀이 있다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다.
구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다.
이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하라.
다음의 4 × 5 얼음 틀 예시에서는 아이스크림이 총 3개가 생성된다


입력
첫 번째 줄에 얼음 틀의 세로 길이 N과 가로 길이 M이 주어진다. (1 <= N, M <= 1,000)
두 번째 줄부터 N + 1 번째 줄까지 얼음 틀의 형태가 주어진다.
이때 구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1이다.
출력
한 번에 만들 수 있는 아이스크림의 개수를 출력한다.

입력 예시 1

4 5
00110
00011
11111
00000
출력 예시 1

3

입력 예시 2

15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
출력 예시2

8
"""

import sys
from collections import deque
y, x = map(int, sys.stdin.readline().rstrip().split())

cur_x = 0
cur_y = 0

icecream_map = [[int(j) for j in sys.stdin.readline().rstrip()] for _ in range(y)]
visited_map = [[bool(j) for j in i] for i in icecream_map]

def dfs(icecream, start_x, start_y, visited_map):
    visited_map[start_y][start_x] = True
    print(start_x, start_y)
    for i in icecream:
        for j in icecream[i]:
            if not visited_map[i][j]:
                dfs(icecream, j, i, visited_map)

dfs(icecream_map, cur_x, cur_y, visited_map)



# 해결 방법
# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1

print(result) # 정답 출력
