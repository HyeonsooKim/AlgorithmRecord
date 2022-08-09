#풀지 못한 문제
"""
떡볶이 떡 만들기
문제
오늘 동빈이는 여행 가신 부모님을 대신해서 떡집 일을 하기로 했다.
오늘은 떡볶이 떡을 만드는 날이다.
동빈이네 떡볶이 떡은 재밌게도 떡볶이 떡의 길이가 일정하지 않다.
대신에 한 봉지 안에 들어가는 떡의 총 길이는 절단기로 잘라서 맞춰준다.
절단기에 높이(H)를 지정하면 줄지어진 떡을 한 번에 절단한다.
높이가 H보다 긴 떡은 H 위의 부분이 잘릴 것이고, 낮은 떡은 잘리지 않는다.
예를 들어 높이가 19, 14, 10, 17cm 인 떡이 나란히 있고 절단기 높이를 15cm로 지정하면
자른 뒤 떡의 높이는 15, 14, 10, 15cm가 될 것이다.
잘린 떡의 길이는 차례대로 4, 0, 0, 2cm이다.
손님은 6cm만큼의 길이를 가져간다.
손님이 왔을 때 요청한 총 길이가 M일 때, 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하세요.

입력 조건
첫째 줄에 떡의 개수 N과 요청한 떡의 길이 M이 주어진다. (1 <= N <= 1,000,000, 1 <= M <= 2,000,000,000)
둘째 줄에는 떡의 개별 높이가 주어진다. 떡 높이의 총합은 항상 M 이상이므로, 손님은 필요한 양만큼 떡을 사갈 수 있다.
높이는 10억보다 작거나 같은 양의 정수 또는 0 이다.

출력 조건
적어도 M만큼의 떡을 집에 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값을 출력한다.

입력 예시
4 6
19 15 10 17

출력 예시
15
"""
import sys
n , m = map(int, sys.stdin.readline().rstrip().split())
ls = list(map(int, sys.stdin.readline().rstrip().split()))

start = 0
end = max(ls)

result = 0
while start <= end:
    mid = (start + end) // 2
    sum_value = sum(list(map(lambda x: x-mid if x > mid else 0, ls)))
    if sum_value < m:
        end = mid - 1
    else:
        start = mid + 1
        result = mid

print(result)



# 해결 방법
import sys
# 떡의 개수 N과 요청한 떡의 길이 M 입력 받기
n, m = map(int, sys.stdin.readline().rstrip().split())
# 떡의 개별 높이 입력 받기
n_list = list(map(int, sys.stdin.readline().rstrip().split()))

# 이진 탐색 시작 위치와 종료 위치 초기화
start = 0
end = max(n_list)

# 절단기의 높이
result = 0

while (start < end):

    # 절단기 높이 지정
    mid = (start+end)//2

    sum = 0
    # 절단기로 모든 떡을 잘랐을 때, 남은 떡의 길이 계산
    for n in n_list:
        # 떡의 높이가 더 높을 때만 자를 수 있음
        if (n > mid):
            sum += n - mid

    # 남은 떡의 길이가 손님이 요청한 떡의 길이보다 적을 경우, 
    # 절단기의 높이를 낮춰야함
    if (sum < m):
        end = mid - 1

    # 남은 떡의 길이가 손님이 요청한 떡의 길이보다 많거나 같을 경우, 
    # 해당 절단기의 높이를 기록하고, 절단기의 높이를 높여야함
    else:
        result = mid
        start = mid + 1

print(result)
    



