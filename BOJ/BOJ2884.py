def main():
    h,m = map(int, input().split(" "))
    if m - 45 < 0:
        h = h - 1 if h - 1 >= 0 else 24 + h - 1 
        m = 60 + (m - 45)
    else:
        m = m - 45
    print(h,m)
if __name__ == '__main__':
    main()