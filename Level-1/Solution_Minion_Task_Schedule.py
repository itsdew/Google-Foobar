#Minion Task Schedule

def solution(data, n):
    new = []
    if len(data) < 100:
        for d in data:
            if n <= 1:
                if data.count(d) > n:
                    pass
                elif data.count(d) <= n:
                    new.append(d)
            elif n > 1:
                if data.count(d) > n:
                    pass
                elif data.count(d) <= n:
                    new.append(d)
    return new