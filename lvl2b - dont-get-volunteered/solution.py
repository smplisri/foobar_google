
import logging

def possible_Coordinates():
    positions = {}
    for i in range(0, 64):
        tmp = []
        ## Side way L shape
        if i - 1 >= 0:
            if i % 8 >= 1:
                if i-1 + (2*8) < 63:
                    tmp.append(i-1 + (2*8))
                if i-1 - (2*8) >= 0:
                    tmp.append(i-1 - (2*8))
        if i + 1 <= 63:
            if i % 8 <= 6:
                if i+1 + (2*8) <= 63:
                    tmp.append(i+1 + (2*8))
                if i+1 - (2*8) > 0:
                    tmp.append(i+1 - (2*8))
        ## Top-bottom L shape
        if i - 8 >= 0:
            if i % 8 <= 5:
                tmp.append(i-8 + 2)
            if i - 10 >= 0 and i % 8 >= 2:
                tmp.append(i-10)
        if i + 8 <= 63:
            if i % 8 >= 2:
                tmp.append(i+8 - 2)
            if i + 10 <= 63 and i % 8 <= 5:
                tmp.append(i+10)
        positions[i] = tmp
    return positions

def dest_finder(coordinates, level, dest, hop, traversed):
    next_level = set()
    for item in level:
        if dest in next_level:
            return hop + 1
        else:
            next_level.update(coordinates[item])
    final_list = [ item for item in next_level if item not in traversed ]
    return dest_finder(coordinates, final_list, dest, hop+1, traversed)

def solution(src, dest):
    log = logging.getLogger
    #Your code here
    coordinates = possible_Coordinates()
    if dest in coordinates[src]:
        return 1
    hops = dest_finder(coordinates, coordinates[src], dest, hop=1, traversed={src})
    return hops if hops is not None else 0

if __name__ == '__main__':
    print(solution(0,1))
    print(solution(19,36))
    print(solution(0,7))
    print(solution(0,56))