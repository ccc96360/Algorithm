def mSum(n):
    s = str(n)
    if len(s) == 1:
        s = "0"+s
    return int(s[0]) + int(s[1])

def newNum(n):
    r = mSum(n) % 10
    l = n % 10
    return int(str(l) + str(r))
    
def main():
    n = int(input())
    cnt = 1
    n2 = newNum(n)
    while n != n2:
        n2 = newNum(n2)
        cnt += 1
    print(cnt)
if __name__ == '__main__':
    main()