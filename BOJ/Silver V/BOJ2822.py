#BOJ2822 점수 계산  20210128
import sys
input = sys.stdin.readline

def main():
    li = sorted([[int(input()), i+1] for i in range(8)], key = lambda x : x[0], reverse=True)
    score = [i[0] for i in li][:5]
    problem = sorted([i[1] for i in li][:5])
    print(sum(score))
    print(*problem)
    
if __name__ == '__main__':
    main()