#Author: Tania Rebello - Farewell until we code again iamhiphopkids ♥
#bfs approach
def solution(map):
    a = pathlength(map)
    b = exit(pathlength(exit(map)))
    return min([sum(v) - 1 for i, _ in enumerate(map) for v in zip(a[i], b[i])])
    
    
def pathlength(map):
    count1 = [
        [1 if i == j == 0 else 999 for j in xrange(len(row))]
        for i, row in enumerate(map)
    ]

    count2 = [(0, 0)]
    while count2:
        a1, b1 = count2.pop(0)
        for move in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            a2, b2 = a1 + move[0], b1 + move[1]
            if 0 <= a2 < len(count1) and 0 <= b2 < len(count1[0]):
                if count1[a2][b2] == 999:
                    count1[a2][b2] = count1[a1][b1] + 1
                    if not map[a2][b2]: count2.append((a2, b2))
    return count1


def exit(map):
    return [[v for v in reversed(row)] for row in reversed(map)]
    
