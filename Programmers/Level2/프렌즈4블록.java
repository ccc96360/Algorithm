//프렌즈4블록 2018 카카오 BLIND RECRUITMENT 20211001
class Solution {
    int tr, tc;
    final char EMPTY = '0';
    public int solution(int m, int n, String[] board) {
        int answer = 0;
        tr = m;
        tc = n;
        char[][] map = makeMap(board);

        while (true){
            boolean[][] deleteP = new boolean[tr][tc];
            boolean hasChange = false;
            
            for(int r = 0; r < tr; r++){
                for(int c = 0; c < tc; c++){
                    if(canDelete(map, r, c)){
                        addDeleteP(deleteP, r, c);
                        hasChange = true;
                    }
                }
            }
            if(!hasChange) break;
            answer += removeBlock(map, deleteP);
            updateBlock(map);
        }

        return answer;
    }

    private void updateBlock(char[][] map) {
        for(int c = 0; c < tc; c++){
            for(int r = tr - 1; r >= 0; r--){
                if(map[r][c] == EMPTY){
                    int sr = r;
                    while(sr >= 0 && map[sr][c] == EMPTY) sr--;
                    if(sr >= 0) {
                        map[r][c] = map[sr][c];
                        map[sr][c] = EMPTY;
                    }else{
                        break;
                    }
                }
            }
        }
    }

    private int removeBlock(char[][] map, boolean[][] deleteP) {
        int ret = 0;
        for(int r = 0; r < tr; r++){
            for(int c = 0; c < tc; c++) {
                if(deleteP[r][c]) {
                    map[r][c] = EMPTY;
                    ret++;
                }
            }
        }
        return ret;
    }

    private void addDeleteP(boolean[][] deleteP, int r, int c) {
        deleteP[r][c] = true;
        deleteP[r][c+1] = true;
        deleteP[r+1][c] = true;
        deleteP[r+1][c+1] = true;
    }

    private boolean canDelete(char[][] map, int r, int c) {
        char v= map[r][c];
        if(v == EMPTY) return false;
        if(r < tr - 1 && c < tc - 1){
            return (v == map[r+1][c] && v == map[r][c+1] && v == map[r+1][c+1]);
        }else{
            return false;
        }
    }

    private char[][] makeMap(String[] board) {
        char[][] ret = new char[tr][];
        for(int r = 0; r < tr; r++){
            ret[r] = board[r].toCharArray();
        }
        return ret;
    }
}