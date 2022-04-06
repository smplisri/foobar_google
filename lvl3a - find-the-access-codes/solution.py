from itertools import combinations as c

def solution(l):
    n = len(l)
    arr = [0] * n
    for i in range(n):
        for j in range(i+1, n):
            if l[j] % l[i] == 0:
                arr[i] += 1
    res = 0
    for i in range(n):
        for j in range(i+1, n):
            if l[j] % l[i] == 0:
                res += arr[j]
    return res

if __name__ == '__main__':
    assert(solution([1,2,3,4,5,6,7,8]) == 6)
