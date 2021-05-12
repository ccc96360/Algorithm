#BOJ11758 CCW 20210512
import sys
input = sys.stdin.readline

X = 0
Y = 1
def ccw(p1, p2, p3):
    tmp = p1[X] * p2[Y] + p2[X] * p3[Y] + p3[X] * p1[Y]
    tmp -= p1[Y] * p2[X] + p2[Y] * p3[X] + p3[Y] * p1[X]
    # tmp는 삼각형의 면적
    return 1 if tmp > 0 else -1 if tmp < 0 else 0

def main():
    p1, p2, p3 = [tuple(map(int,input().rstrip().split())) for _ in range(3)]
    print(ccw(p1,p2,p3))
        
if __name__ == '__main__':
    main()