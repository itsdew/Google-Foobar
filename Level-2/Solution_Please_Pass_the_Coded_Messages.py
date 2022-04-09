#Devendra Uraon
def solution(l):
    l = sorted(l, reverse = True)
    if sum(l) % 3 == 0:
        return int("".join(str(n) for n in l))
    ans = [0]
    for i in range(len(l)):
        count = l[:]
        del count[len(count) - i - 1]
        if sum(count) % 3 == 0:
            return int("".join(str(n) for n in count))
        for j in range(1, len(count)):
            count2 = count[:]
            del count2[len(count2) - j - 1]
            if sum(count2) % 3 == 0:
                ans.append(int("".join(str(n) for n in count2)))
    return max(ans)