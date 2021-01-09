def main():
    x,y,w,h = map(int, input().split(' '))
    n = w - x
    e = h - y
    res = min(min(x,y), min(n,e))
    print(res)
if __name__ == '__main__':
    main()
