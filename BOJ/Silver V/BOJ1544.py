#BOJ1544 사이클 단어 20210122 
def find(a,b):
    sIdx = []
    n = len(a)
    if n != len(b) : return False
    for i in range(n):
        if a[0] == b[i]:
            sIdx.append(i)
    ret = False
    for i in sIdx:
        tmp = i
        cnt = 0
        for j in range(n):
            if a[j] == b[tmp]: cnt += 1
            tmp = (tmp + 1) % n
        if cnt == n:
            ret = True
            break
    return ret

def main():
    li = []
    n = int(input())
    li.append(input())
    for _ in range(1,n):
        tmp = input()
        flag = False
        for s in li:
            if find(s,tmp):
                flag = True
        if not flag:
            li.append(tmp)
    print(len(li))

if __name__ == '__main__':
    main()