//BOJ1039 교환 20210705
import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

import static java.lang.Math.max;

public class Main {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    private static int n,m;
    private static String[][] board;
    private static int[][] visited;
    private static int[][] dp;


    private static int[] dr = {-1,0,1,0};
    private static int[] dc = {0,1,0,-1};

    public static void main(String[] args) throws IOException {
        StringTokenizer stk = new StringTokenizer(br.readLine());
        String[] n = stk.nextToken().split("");
        int k = Integer.parseInt(stk.nextToken());

        Map<Integer, Set<Integer>> visited = new HashMap<>();
        Queue<int[]> q = new LinkedList<>();

        int intN = stringArrToInt(n);
        for(int i = 0; i <= 10; i++){
            visited.put(i, new HashSet<>());
        }
        visited.get(0).add(intN);
        q.add(new int[]{intN,0});

        int ans = -1;
        while (!q.isEmpty()){
            int[] info = q.poll();
            String[] v = intToStringArr(info[0]);
            int cnt = info[1];

            if(cnt == k){
                ans = max(ans, info[0]);
                continue;
            }
            int size = v.length;
            for(int i = 0; i < size; i++){
                for(int j = i+1; j < size; j++){
                    String tmp = v[j];
                    v[j] = v[i];
                    v[i] = tmp;

                    if(v[0].equals("0")){
                        v[i] = v[j];
                        v[j] = tmp;
                        continue;
                    }
                    int nextNum = stringArrToInt(v);
                    if(!visited.get(cnt+1).contains(nextNum)){
                        q.add(new int[]{nextNum, cnt+1});
                        visited.get(cnt+1).add(nextNum);
                    }
                    v[i] = v[j];
                    v[j] = tmp;
                }
            }
        }
        System.out.println(ans);
    }

    public static int stringArrToInt(String[] arr){
        return Integer.parseInt(Arrays.stream(arr).collect(Collectors.joining()));
    }
    public static String[] intToStringArr(int n){
        return Integer.toString(n).split("");
    }
}