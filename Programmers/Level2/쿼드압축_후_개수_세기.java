//쿼드압축 후 개수 세기 월간 코드 챌린지 시즌1 20211008
class Solution {

    int[][] board;
    
    public int[] solution(int[][] arr) {
        int n = arr.length;
        board = arr;
        return solve(0, 0, n);
    }

    private int[] solve(int sr, int sc, int n){
        int[] ret = {0, 0};
        if(isAllSame(sr, sc, n)){
            ret[board[sr][sc]]++;
            return ret;
        }
        int[] dr = {0, 0, n / 2, n / 2};
        int[] dc = {0, n / 2, 0, n / 2};
        for(int i = 0; i < 4; i++){
            int nr = sr + dr[i], nc = sc + dc[i];
            int[] tmp = solve(nr, nc, n / 2);
            ret[0] += tmp[0];
            ret[1] += tmp[1];
        }
        return ret;
    }

    private boolean isAllSame(int sr, int sc, int n){
        int v = board[sr][sc];
        for(int r = sr; r < sr + n; r++){
            for(int c = sc; c < sc + n; c++){
                if(board[r][c] != v) return false;
            }
        }
        return true;
    }
}