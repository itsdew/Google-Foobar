#Devendra Uraon 
def solution(data, n):
    ans = []
    if len(data) < 100:
        for d in data:
            if n <= 1:
                if data.count(d) > n:
                    pass
                elif data.count(d) <= n:
                    ans.append(d)
            elif n > 1:
                if data.count(d) > n:
                    pass
                elif data.count(d) <= n:
                    ans.append(d)
    return ans
