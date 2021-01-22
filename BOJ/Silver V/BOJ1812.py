#BOJ1812 사탕 20210122  
def main():
    n = int(input())
    li = [int(input()) for _ in range(n)]
    s = sum(li) // 2
    res = [0] * n
    for i in range(n):
        idx = 0 if i % 2 == 0 else 1
        if i == 0 : idx = 1
        if i == 1 : idx = 2
        for j in range(n//2):
            res[i] += li[idx]
            idx += 2
            if i == idx: idx += 1
        res[i] = str(s - res[i])
    print("\n".join(res))
if __name__ == '__main__':
    main()