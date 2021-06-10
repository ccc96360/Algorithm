#BOJ2310 어드벤처 게임 20210610
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(v, money, rooms, roomInfo, dst, visited):
    type, cost = roomInfo[v]
    if type == "L":
        if money <= cost: money = cost
    elif type == "T":
        if money < cost:
            return "No"
        else:
            money -= cost
    if v == dst:
        return "Yes"
    ret = "No"
    for nv in rooms[v]:
        if not visited[nv]:
            visited[nv] = True
            ret = dfs(nv, money, rooms, roomInfo, dst, visited)
            visited[nv] = False
            if ret == "Yes":
                break
    return ret
def main():
    while True:
        n = int(input())
        if n == 0: break
        rooms = [[] for _ in range(n+1)]
        roomInfo = [[0,0] for _ in range(n+1)]
        for i in range(1, n+1):
            roomType, cost, *info = input().rstrip().split()
            roomInfo[i][0] = roomType
            roomInfo[i][1] = int(cost)
            rooms[i].extend(list(map(int, info[:-1])))
        
        visited = [False] * (n+1)
        visited[1] = True
        print(dfs(1, 0, rooms, roomInfo, n, visited))
if __name__ == '__main__':
    main()