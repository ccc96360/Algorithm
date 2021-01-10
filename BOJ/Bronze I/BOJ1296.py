def prob(a,b):
    L = a["L"] + b["L"]
    O = a["O"] + b["O"]
    V = a["V"] + b["V"]
    E = a["E"] + b["E"]
    return ((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E)) % 100
 
def main():
    mName = input()
    mNum = {"L" : 0, "O" : 0, "V" : 0, "E" : 0}
    for s in mName:
        if s in mNum:
            mNum[s] += 1
    n = int(input())
    max = -1
    res = ""
    names = [input() for _ in range(n)]
    names.sort()
    for name in names:
        num = {"L" : 0, "O" : 0, "V" : 0, "E" : 0}
        for s in name:
            if s in num:
                num[s] += 1
        p = prob(mNum, num)
        if p > max:
            max = p
            res = name
    print(res)
if __name__ == '__main__':
    main()