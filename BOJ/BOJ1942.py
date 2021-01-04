def isMulOfThr(h, m, s):
    tmp = int(str(h) + str(m) + str(s))
    return True if tmp % 3 == 0 else False

def nextTime(h,m,s):
    s += 1
    if s == 60:
        s = 0
        m += 1
    if m == 60:
        m = 0
        h += 1
    if h == 24:
        h = 0
    return h, m, s

def main():
    for i in range(3):
        s,e = input().split(" ")
        h1,m1,s1 = map(int, s.split(":"))
        h2,m2,s2 = map(int, e.split(":"))
        res = 0
        while not (h1 == h2 and m1 == m2 and s1 == s2):
            if isMulOfThr(h1, m1, s1):
                res += 1
            h1, m1, s1 = nextTime(h1, m1, s1)
        if isMulOfThr(h1,m1,s1):
            res += 1
        print(res)
if __name__ == '__main__':
    main()