//BOJ15686 치킨 배달 20210706
import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

import static java.lang.Math.*;

public class Main {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    private static int[][] board;
    private static int n;
    private static int m;
    private static int ans = Integer.MAX_VALUE;

    private static List<int[]> homes;
    private static List<int[]> chicken;
    private static Map<int[], Map<int[], Integer>> chickenDistance;

    public static void main(String[] args) throws IOException {
        StringTokenizer stk = new StringTokenizer(br.readLine());
        n = Integer.parseInt(stk.nextToken());
        m = Integer.parseInt(stk.nextToken());

        board = new int[n][n];

        for(int i = 0; i < n; i++){
            board[i] = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        }

        homes = new ArrayList<>();
        chicken = new ArrayList<>();
        chickenDistance = new HashMap<>();

        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if(board[i][j] == 1){
                    homes.add(new int[]{i,j});
                }
                else if(board[i][j] == 2){
                    chicken.add(new int[]{i,j});
                }
            }
        }

        for(int[] home: homes){
            chickenDistance.put(home, new HashMap<>());
            for(int[] point: chicken){
                chickenDistance.get(home).put(point,getDistance(home,point));
            }
        }

        dfs(0, chicken.size(), new Stack<>());

        System.out.println(ans);
        bw.flush();
        bw.close();
    }

    public static void dfs(int v, int size, Stack<int[]> selected){
        if(selected.size() == m){
            int ret = 0;
            for(int[] home: homes){
                int min = Integer.MAX_VALUE;
                for(int[] point: selected){
                    min = min(chickenDistance.get(home).get(point), min);
                }
                ret += min;
            }
            ans = min(ret, ans);
            return;
        }
        for(int i = v; i < size; i++){
            selected.push(chicken.get(i));
            dfs(i+1, size, selected);
            selected.pop();
        }
    }
    public static int getDistance(int[] a, int[] b){
        return abs(a[0] - b[0]) + abs(a[1] - b[1]);
    }
}