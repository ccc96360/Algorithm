//BOJ3055 탈출 20210705
import java.io.*;
import java.util.*;

public class BOJ3055 {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    public static void main(String[] args) throws IOException {
        StringTokenizer stk = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(stk.nextToken());
        int m = Integer.parseInt(stk.nextToken());

        String[][] board = new String[n][m];
        for(int i = 0; i < n; i++){
            board[i] = br.readLine().split("");
        }


        Queue<int[]> gosumLoc = new LinkedList<>();
        Queue<int[]> waterQ = new LinkedList<>();
        int[] cave = new int[2];
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j ++){
                if(board[i][j].equals("S")){
                    gosumLoc.add(new int[]{i,j});
                    board[i][j] = "S0";
                }
                else if(board[i][j].equals("D")){
                    cave = new int[]{i,j};
                }
                else if(board[i][j].equals("*")){
                   waterQ.add(new int[]{i,j});
                   board[i][j] = "*0";
                }
            }
        }

        int[] dr = {-1, 0, 1, 0};
        int[] dc = {0, 1, 0, -1};
        int time = 0;
        boolean flag = false;

        while(!gosumLoc.isEmpty() || !waterQ.isEmpty()){
            if(flag) break;
            while(!waterQ.isEmpty()){
                int[] pos = waterQ.peek();
                int r = pos[0], c = pos[1];
                if(!board[r][c].equals("*" + time)) break;
                waterQ.poll();
                for(int i = 0; i < 4; i++){
                    int nr = r + dr[i];
                    int nc = c + dc[i];
                    if((0 <= nr && nr < n) && (0 <= nc && nc < m)){
                        if(board[nr][nc].equals(".")){
                            board[nr][nc] = "*" + (time + 1);
                            waterQ.add(new int[]{nr, nc});
                        }
                    }
                }
            }

            while(!gosumLoc.isEmpty()){
                int[] pos = gosumLoc.peek();
                int r = pos[0], c = pos[1];
                if(!board[r][c].equals("S" + time)) break;
                gosumLoc.poll();

                for(int i = 0; i < 4; i++){
                    int nr = r + dr[i];
                    int nc = c + dc[i];
                    if((0 <= nr && nr < n) && (0 <= nc && nc < m)){
                        if(board[nr][nc].equals("D")){
                            board[nr][nc] = Integer.toString(time+1);
                            flag = true;
                        }
                        if(board[nr][nc].equals(".")){
                            board[nr][nc] = "S" + (time + 1);
                            gosumLoc.add(new int[]{nr,nc});
                        }
                    }
                }
            }
            time++;
        }
        String ret = board[cave[0]][cave[1]];
        if(ret.equals("D")){
            bw.write("KAKTUS\n");
        }else{
            bw.write(ret + "\n");
        }

        bw.flush();
        bw.close();
    }
}