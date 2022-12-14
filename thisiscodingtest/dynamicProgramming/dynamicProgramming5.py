"""
[문제]
N명의 병사가 무작위로 나열되어 있습니다. 각 병사는 특정한 값의 전투력을 보유하고 있습니다.

 

병사를 배치할 때는 전투력이 높은 병사가 앞쪽에 오도록 내림차순으로 배치를 하고자 합니다. 

 

다시 말해 앞쪽에 있는 병사의 전투력이 항상 뒤쪽에 있는 병사보다 높아야 합니다.

 

또한 배치 과정에서는 특정한 위치에 있는 병사를 열외시키는 방법을 이용합니다. 그러면서도 남아 있는 병사의 수가

 

최대가 되도록 하고 싶습니다. 예를 들어, N = 7일 때 나열된 병사들의 전투력이 다음과 같다고 가정하겠습니다.

 

병사 번호	1	2	3	4	5	6	7
전투력	15	11	4	8	5	2	4
 

이때 3번 병사와 6번 병사를 열외시키면, 다음과 같이 남아 있는 병사의 수가 내림차순의 형태가 되며 5명이 됩니다.

 

이는 남아 있는 병사의 수가 최대가 되도록 하는 방법입니다.

 

병사 번호	1	2	4	5	7
전투력	15	11	8	5	4
 

병사에 대한 정보가 주어졌을 때, 남아 있는 병사의 수가 최대가 되도록 하기 위해서 열외시켜야 하는 병사의 수를

 

출력하는 프로그램을 작성하세요.

 

[입력 조건]
1. 첫째 줄에 N이 주어집니다. (1 <= N <= 2,000)

 

2. 둘째 줄에 병사의 전투력이 공백으로 구분되어 차례대로 주어집니다. 각 병사의 전투력은 10,000,000보다 작거나 같은 자연수입니다.

 

[출력 조건]
첫째 줄에 남아 있는 병사의 수가 최대가 되도록 하기 위해서 열외시켜야 하는 병사의 수를 출력합니다.

<입력 예시>
7
15 11 4 8 5 2 4
<출력 예시>
2
"""
# 기본 아이디어 - 가장 긴 증가하는 부분 수열(Longest Increasing Subsequence, LIS)
# -> 모든 0<=j < i에 대해, DP[i] = max(DP[i], DP[j] + 1) if array[j] < array[i] 
# 병사의 수 - 2000이하 - O(n^2)까지 선택가능
n = int(input())

arr = list(map(int, input().split()))

d = [0] * len(arr)
d[0] = arr[0]
for i in range(1, len(arr)):
    for j in range(i):
        d[i] = max(d[i], d[j]+1) if (arr[j] > arr[i])

print(d[n-1])


# 해결 방법
n = int(input())
arr = list(map(int, input().split()))
# 순서를 뒤집어 '최장 증가 부분 수열' 문제로 변환
arr.reverse()

# 다이나믹 프로그래밍을 위한 1차워 DP 테이블 초기화
dp = [1] * n

# 가장 긴 증가하는 부분 수열(LIS) 알고리즘 수행
for i in range(1, n):
    for j in range(0, i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j]+1)

# 열외해야 하는 병사의 최소 수를 출력
print(n - max(dp))

