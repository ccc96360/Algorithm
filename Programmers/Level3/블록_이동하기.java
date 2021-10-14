//블록 이동하기 2021 카카오 BLIND RECRUITMNET 20211014
import java.util.*;

class Solution {
    
    final int GARO = 1, SERO = 2, FIRST = 1, SECOND = 2, CW = 1, CCW = 2;
    final int RIGHT = 1, LEFT = 2, UP = 3, DOWN = 4;
    int[] rotateDirs = {CW, CCW};
    int[] axises = {FIRST, SECOND};
    int[] moveDirs = {RIGHT, LEFT, UP, DOWN};
    int[] cant = {-1};
    
    int n;
    int[][] board;
    public int solution(int[][] qwer) {
        int answer = 0;
        
        n = qwer.length;
        board = qwer;
        
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{0, 0, 0, 1, 0});
        
        boolean[][][][] visited = new boolean[n][n][n][n];
        visited[0][0][0][1] = true;
        while(!q.isEmpty()){
            int[] pos = q.poll();
            if(pos[2] == n - 1 && pos[3] == n - 1){
                answer = pos[4];
                break;
            }
            //상하좌우
            for(int moveDir : moveDirs){
                int[] res = move(moveDir, pos);
                if(validation(res, visited)){
                    q.add(res);
                }
                    
            }
            
            //회전
            for(int rotateDir : rotateDirs){
                for(int axis : axises){
                    int[] res = rotate(rotateDir, axis, pos);
                    if(validation(res, visited)){
                        q.add(res);
                    }
                }
            }
            
        }
        
        
        return answer;
    }
    
    boolean validation(int[] pos, boolean[][][][] visited){
        if(pos[0] == -1) return false;
        int fr = pos[0], fc = pos[1], sr = pos[2], sc = pos[3];
        if(visited[fr][fc][sr][sc]) return false;
        visited[fr][fc][sr][sc] = true;
        return true;
    }    
    
    int[] move(int dir, int[] pos){
        int fr = pos[0], fc = pos[1], sr = pos[2], sc = pos[3], time = pos[4];
        int nfr = pos[0], nfc = pos[1], nsr = pos[2], nsc = pos[3];
        int[] ret;
        if(dir == LEFT){
            if(fc == 0) return cant;
            nfc = fc - 1;
            nsc = sc - 1;
        }else if(dir == RIGHT){
            if(sc == n - 1) return cant;
            nfc = fc + 1;
            nsc = sc + 1;
        }else if(dir == UP){
            if(fr == 0) return cant;
            nfr = fr - 1;
            nsr = sr - 1;
        }else if(dir == DOWN){
            if(sr == n - 1) return cant;
            nfr = fr + 1;
            nsr = sr + 1;
        }else{
            return cant;
        }
        if(board[nfr][nfc] == 1 || board[nsr][nsc] == 1) return cant;
        return new int[]{nfr, nfc, nsr, nsc, time  + 1};
    }
    
    int[] rotate(int dir, int axis, int[] pos){
        return (dir == CW)? rotateCW(axis, pos) : rotateCCW(axis, pos); 
    }
    
    int[] rotateCW(int axis, int[] pos){
        int direction = getDirection(pos), time = pos[4];
        if(direction == GARO){
            int r = pos[0], lc = pos[1], rc = pos[3];
            if(axis == FIRST && r < n - 1){
                if(board[r + 1][lc] == 0 && board[r + 1][rc] == 0){
                    return new int[]{r, lc, r + 1, lc, time + 1};
                }
            }else if(r > 0){
                if(board[r - 1][lc] == 0 && board[r - 1][rc] == 0){
                    return new int[]{r - 1, rc, r, rc, time + 1};
                }
            }
            return cant;
        }else{
            int c = pos[1], tr = pos[0], br = pos[2];
            if(axis == FIRST && c > 0){ 
                if(board[tr][c- 1] == 0 && board[br][c - 1] == 0)
                    return new int[]{tr, c - 1, tr, c, time + 1};
            } else if(c < n - 1){
                if(board[tr][c + 1] == 0 && board[br][c + 1] == 0)
                    return new int[]{br, c, br, c + 1, time + 1};
            }
            return cant;
        }
    }
    
    int[] rotateCCW(int axis, int[] pos){
        int direction = getDirection(pos), time = pos[4];
        if(direction == GARO){
            int r = pos[0], lc = pos[1], rc = pos[3];
            if(axis == FIRST && r > 0){
                if(board[r - 1][lc] == 0 && board[r - 1][rc] == 0){
                    return new int[]{r - 1, lc, r, lc, time + 1};
                }
            }else if(r < n - 1){
                if(board[r + 1][lc] == 0 && board[r + 1][rc] == 0){
                    return new int[]{r, rc, r + 1, rc, time + 1};
                }
            }
            return cant;
        }else{
            int c = pos[1], tr = pos[0], br = pos[2];
            if(axis == FIRST && c < n - 1){ 
                if(board[tr][c + 1] == 0 && board[br][c + 1] == 0)
                    return new int[]{tr, c, tr, c + 1, time + 1};
            } else if(c > 0){
                if(board[br][c - 1] == 0 && board[tr][c - 1] == 0)
                    return new int[]{br, c - 1, br, c, time + 1};
            }
            return cant;
        }
        
    }
    
    int getDirection(int[] pos){
        return (pos[0] == pos[2])? GARO : SERO;
    }
}