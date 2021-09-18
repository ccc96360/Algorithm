def isRight(p):
    l = 0
    for v in p:
        if v == "(": l += 1
        else:
            if l > 0:
                l -= 1
            else:
                return False
    if l != 0: return False
    return True

def solve(p):
    if p == "":
        return p
    if isRight(p):
        return p
    l = r = 0
    u = ""
    v = ""
    for i in range(len(p)):
        if p[i] == "(": l += 1
        if p[i] == ")": r += 1
        if l == r:
            u = p[:i+1]
            v = p[i+1:]
            break
    if isRight(u):
        return u + solve(v)
    else:
        tmp = "(" + solve(v) + ")"
        u = u[1:-1]
        tmp += "".join(list(map(lambda x: "(" if x == ")" else ")", u)))
        return tmp
        
def solution(p):
    return solve(p)

def main():
    p = "()))((()"
    print(solution(p))

if __name__ == '__main__':
    main()