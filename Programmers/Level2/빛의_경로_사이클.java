//빛의 경로 사이클 월간 코드 챌린지 시즌3 20210925
import java.util.*;

class Solution {

    String[][] board;
    int row, col;
    final int UP = 0, RIGHT = 1, DOWN = 2, LEFT = 3;
    int[] turnLeft = new int[]{3, 0, 1, 2};
    int[] turnRight = new int[]{1, 2, 3, 0};

    public int[] solution(String[] grid) {
        List<Integer> ans = new ArrayList<>();

        board = makeBoard(grid);
        boolean[][][] visited = new boolean[row][col][4];
        for (int r = 0; r < row; r++) {
            for (int c = 0; c < col; c++) {
                for (int i = 0; i < 4; i++) {
                    if (!visited[r][c][i]) {
                        ans.add(solve(r, c, i, visited));
                    }
                }
            }
        }


        return ans.stream().sorted().mapToInt(Integer::intValue).toArray();
    }

    public int solve(int r, int c, int dir, boolean[][][] visited){
        int ret = 0;
        while(!visited[r][c][dir]){
            visited[r][c][dir] = true;
            ret++;

            int[] nextPos = getNextPos(r, c, dir);
            r = nextPos[0];
            c = nextPos[1];
            dir = nextPos[2];
        }
        return ret;
    }

    public int[] getNextPos(int r, int c, int dir){
        int nr = r, nc = c;
        if(dir == UP){
            nr = (r != 0) ? (r - 1) : (row - 1);
        }else if(dir == DOWN){
            nr = (r != row - 1) ? (r + 1) : 0;
        }else if(dir == LEFT){
            nc = (c != 0) ? (c - 1) : (col - 1);
        }else{
            nc = (c != col - 1) ? (c + 1) : 0;
        }
        return new int[]{nr, nc, getNextDir(nr, nc, dir)};
    }

    private int getNextDir(int r, int c, int prevDir) {
        int ret = prevDir;
        if(board[r][c].equals("L")){
            ret = turnLeft[prevDir];
        }else if(board[r][c].equals("R")){
            ret = turnRight[prevDir];
        }
        return ret;

    }

    private String[][] makeBoard(String[] grid) {
        row = grid.length;
        col = grid[0].length();

        String[][] board = new String[row][col];
        for (int i = 0; i < row; i++) {
            board[i] = grid[i].split("");
        }

        return board;
    }
}