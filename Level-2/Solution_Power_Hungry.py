#Devendra Uraon
def solution(xs):
    ans = 1
    if(xs.count(0) == len(xs)): return(str(0))
    if(len(xs) == 1 and len([n for n in xs if n < 0]) == 1): return(str(xs[0]))
    if(len([n for n in xs if n < 0]) == 1 and xs.count(0) == len(xs)-1): return(str(0))
    for i in xs:
        if (i != 0 and i <= 1000):
            ans *= i
    if ans < 0:
        MaxCount = max([n for n in xs if n < 0])
        ans /= MaxCount

    return(str(int(ans)))