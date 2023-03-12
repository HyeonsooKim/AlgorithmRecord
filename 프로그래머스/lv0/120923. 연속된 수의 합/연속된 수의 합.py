def solution(num, total):
    a = int((2*total/num + 1 - num) / 2)
    return [x for x in range(a, a+num)]