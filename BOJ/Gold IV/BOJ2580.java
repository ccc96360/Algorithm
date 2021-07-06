//BOJ2580 스도쿠 20210706
import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

import static java.lang.Math.max;

public class Main {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    private static int[][] board = new int[9][9];
    private static List<int[]> zeroes;
    private static Map<int[], List<Integer>> cases;

    public static void main(String[] args) throws IOException {
        for(int i = 0; i < 9; i++){
            board[i] = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        }

        zeroes = getZeroes();
        cases = getCases(zeroes);

        dfs(0, zeroes.size());

        for(int i = 0; i < 9; i++){
            for(int j = 0; j < 8; j++){
                bw.write(board[i][j] + " ");
            }
            bw.write(board[i][8] + "\n");
        }

        bw.flush();
        bw.close();
    }

    public static boolean dfs(int v, int end){
        if(v == end) return true;
        int[] point = zeroes.get(v);
        int r = point[0], c = point[1];
        for(int can: cases.get(point)){
            if(isValid(r,c,can)){
                board[r][c] = can;
                if(dfs(v+1, end)) return true;
                board[r][c] = 0;
            }
        }
        return false;
    }

    public static boolean isValid(int r, int c, int v){
        for(int i = 0; i < 9; i++){
            if(board[i][c] == v) return false;
            if(board[r][i] == v) return false;
        }
        int sr = (r/3) * 3;
        int sc = (c/3) * 3;
        for(int i = sr; i < sr + 3; i++){
            for(int j = sc; j < sc + 3; j++){
                if(board[i][j] == v) return false;
            }
        }
        return true;
    }

    public static List<int[]> getZeroes(){
        List<int[]> zeroes = new ArrayList<>();
        for(int i = 0; i < 9; i++){
            for(int j = 0; j < 9; j++){
                if(board[i][j] == 0){
                    zeroes.add(new int[]{i,j});
                }
            }
        }
        return zeroes;
    }

    public static Map<int[], List<Integer>> getCases(List<int[]> zeroes){
        Map<int[], List<Integer>> ret = new HashMap<>();

        for(int[] point: zeroes){
            ret.put(point, new ArrayList<>());
            Set<Integer> cant = new HashSet<>();
            int r = point[0], c = point[1];
            for(int i = 0; i < 9; i++){
                cant.add(board[i][c]);
                cant.add(board[r][i]);
            }
            int sr = (r/3) * 3;
            int sc = (c/3) * 3;
            for(int i = sr; i < sr + 3; i++){
                for(int j = sc; j < sc + 3; j++){
                    cant.add(board[i][j]);
                }
            }
            for(int i = 1; i <= 9; i++){
                if(!cant.contains(i)) ret.get(point).add(i);
            }
        }

        return ret;
    }
}