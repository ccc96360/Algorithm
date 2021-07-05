//BOJ1759 암호 만들기 20210705
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
        int l = Integer.parseInt(stk.nextToken());
        int c = Integer.parseInt(stk.nextToken());
        String[] arr = br.readLine().split(" ");
        Arrays.sort(arr);
        dfs(0, arr, c, l, new String[l], 0);
        bw.flush();
        bw.close();
    }

    public static void dfs(int start, String[] arr, int n, int r, String[] selected, int idx) throws IOException{
        if(r == 0){
            if(isSuitable(selected)) {
                String res = Arrays.stream(selected).collect(Collectors.joining());
                bw.write(res + "\n");
            }
            return;
        }
        for(int i = start; i < n; i++){
            selected[idx] = arr[i];
            dfs(i+1, arr, n, r-1, selected, idx+1);
        }

    }

    private static boolean isSuitable(String[] selected) {
        Set<String> mo = new HashSet<>(Arrays.asList("a", "e", "i", "o", "u"));
        Set<String> containMo = new HashSet<>();
        Set<String> containJa = new HashSet<>();
        for(String v: selected){
            if(mo.contains(v)){
                containMo.add(v);
            }
            else{
                containJa.add(v);
            }
        }
        return  containMo.size() >= 1 && containJa.size() >= 2;
    }
}