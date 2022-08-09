s = 'aAb'
print(s.lower())
print(ord('t'), ord('T'))
print(ord('o'), ord('O'))
print(ord('s'), ord('S'))
print(ord('z'))
import sys
# 알파벳 아스키코드 저장할 배열
alpha = [0] * 123
ls = list(map(str.lower,sys.stdin.readline().rstrip()))
for i in ls:
    alpha[ord(i)] += 1

max_value = max(alpha)
result = []
if alpha[ord('t')] == max_value:
    result.append('T')
if alpha[ord('o')] == max_value:
    result.append('O')
if alpha[ord('s')] == max_value:
    result.append('SS')

for i in range(ord('a'), ord('z')+1):
    if alpha[i] == max_value and i not in [ord('t'), ord('o'), ord('s')]:
        result.append(chr(i))

answer = ''
for i in result:
    answer += i
print(answer)