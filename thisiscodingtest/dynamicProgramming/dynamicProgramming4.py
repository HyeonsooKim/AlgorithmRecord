"""
문제
n x m 크기의 금광이 있다. 금광은 1 x 1 크기의 칸으로 나누어져 있으며, 각 칸은 특정한 크기의 금이 들어 있다.
채굴자는 첫 번째 열부터 출발하여 금을 캐기 시작하는데 맨 처음에는 첫 번째 열의 어느 행에서든 출발할 수 있다.
이후에 m번에 걸쳐서 매번 오른쪽 위, 오른쪽, 오른쪽 아래 3가지 중 하나의 위치로 이동해야 한다.
결과적으로 채굴자가 얻을 수 있는 금의 최대 크기를 출력하는 프로그램을 작성하시오.
 

입력 조건

첫째 줄에 테스트 케이스 T가 입력된다. (1 <= T <= 1,000)
매 테스트 케이스 첫째 줄에 n과 m이 공백으로 구분되어 입력된다. (1 < n, m <= 20)
매 테스트 케이스 둘째 줄에 n x m 위치에 매장된 금의 개수가 공백으로 구분되어 입력된다. (0 이상 100 이하의 정수)
 

출력 조건
테스트 케이스마다 채굴자가 얻을 수 있는 금의 최대 크기를 출력한다.

입력 예시

2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2

출력 예시

19
16
"""
import sys
test_case = int(input())
for i in range(test_case):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    arr = [[arr[i] for i in range(j*4, (j+1)*4)] for j in range(n)]
    print(arr)