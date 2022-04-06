from itertools import permutations

def possibleOutcomes(values, size):
    Outcomes = []
    for item in permutations(values, size):
        Outcomes.append(''.join([ str(x) for x in item]))
    return Outcomes

def solution(l):
    # Your code here
    size = len(l)
    value = None
    while size > 0 and value is None:
        Outcomes = possibleOutcomes(l, size)
        Outcomes.sort(reverse=True)
        for item in Outcomes:
            if int(item)%3 == 0:
                value = item
                break
        size -= 1
    return value

if __name__ == '__main__':
    print(solution([3, 1, 4, 1]))
    print(solution([3, 1, 4, 1, 5, 9]))