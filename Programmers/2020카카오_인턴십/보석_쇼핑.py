def solution(gems):
    own = {}
    for v in gems:
        if v not in own:
            own[v] = 0
    l = r = ownCnt = 0 

    n = len(gems)
    m = len(set(gems))
    res = (0,0,100001)
    while r < n:
        v = gems[r]
        if own[v] == 0: ownCnt += 1
        own[v] += 1
        r += 1
        if ownCnt == m:
            while own[gems[l]] > 1:
                own[gems[l]] -= 1
                l += 1
            if res[2] > r-l:
                res = (l,r,r-l)
    return [res[0]+1,res[1]]