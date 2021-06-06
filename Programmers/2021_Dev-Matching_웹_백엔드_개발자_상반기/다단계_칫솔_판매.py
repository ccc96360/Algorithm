answer = []
def getBenefit(benefit):
    tax = int(benefit * 0.1)
    return benefit - tax, tax

def dfs(v, parents, benefit):
    global answer
    mBenefit, tax = getBenefit(benefit)
    answer[v] += mBenefit
    nv = parents[v]
    if nv != -1 and tax != 0:
        dfs(nv, parents, tax)

def solution(enroll, referral, seller, amount):
    global answer
    n = len(enroll)
    m = len(seller)
    answer = [0] * (n)
    parents = [-1 for _ in range(n)]
    nameToIdx = { enroll[i] : i for i in range(n)}
    for i in range(n):
        v = referral[i]
        if v != "-":
            parents[nameToIdx[enroll[i]]] = nameToIdx[v]
    for i in range(m):
        v = nameToIdx[seller[i]]
        dfs(v, parents, amount[i] * 100)
        
    return answer

def main():
    a = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
    b = ["-"   , "-"   , "mary", "edward", "mary", "mary", "jaimie", "edward"]
    c = ["young", "john", "tod", "emily", "mary"]
    d = [12, 4, 2, 5, 10]
    print(solution(a,b,c,d))
if __name__ == '__main__':
    main()