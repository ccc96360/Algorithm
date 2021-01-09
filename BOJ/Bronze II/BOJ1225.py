def main():
    a,b = input().split(" ")
    sumA = sum(map(int, a))
    sumB = sum(map(int, b))
    print(sumA * sumB)

if __name__ == '__main__':
    main()
