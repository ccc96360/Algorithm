def res(x):
    print(x if x != 0 else 10)

def main():
    T = int(input())
    for t in range(0,T):
        a,b = map(int, input().split(" "))
        arr = [a%10]
        while True:
            tmp = (arr[-1] * a) % 10
            if tmp == arr[0]:
                break
            else:
                arr.append(tmp)
        n = len(arr)
        if n == 1:
            res(arr[0])
        else:
            if b % n == 0:
                res(arr[n-1])
            else:
                res(arr[(b%n)-1])

if __name__ == '__main__':
    main()