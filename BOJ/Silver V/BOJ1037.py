#BOJ1037 약수 20210118
def main():
    n = int(input())
    li = list(map(int, input().split(" ")))
    li.sort()
    print(li[0] * li[-1])
    
if __name__ == '__main__':
    main()