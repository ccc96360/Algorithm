def f(x):
    ret = 1
    for i in x:
        ret *= int(i)
    return ret

def main():
    n = input()
    for i in range(1, len(n)):
        a = n[0:i]
        b = n[i:len(n)+1]
        if f(a) == f(b):
            return print("YES")
    return print("NO")

if __name__ == '__main__':
    main()