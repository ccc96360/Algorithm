def rev(x):
    ret = int("".join(reversed(str(x))))
    return ret

def main():
    a,b = map(int, input().split(" "))
    print(rev(rev(a) + rev(b)))
if __name__ == '__main__':
    main()