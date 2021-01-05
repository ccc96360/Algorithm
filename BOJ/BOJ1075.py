def main():
    n = int(input())
    f = int(input())
    a = (n // 100) * 100
    for i in range(100):
        if a % f == 0:
            break
        a += 1
    res = a % 100
    print(res if res >= 10 else "0"+str(res))
    
if __name__ == '__main__':
    main() 