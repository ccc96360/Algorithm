def main():
    a,b,n = map(int, input().split(" "))
    print(((a*(10**n))//b)%10)
if __name__ == '__main__':
    main()