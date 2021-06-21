//BOJ15652 N과 M (4) 20210621
import java.io.*;
import java.util.*;

public class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static int stoi(String v){
        return Integer.parseInt(v);
    }

    public static void dfs(int idx, int beforIdx, int[] selected, int[] arr, int m, int n) throws IOException {
        if(idx == m){
            for(int v: selected){
                bw.write(v + " ");
            }
            bw.write("\n");
        }
        else {
            for (int i = beforIdx; i < n; i++) {
                selected[idx] = arr[i];
                dfs(idx + 1, i, selected, arr, m, n);
            }
        }
    }
    public static void main(String[] args) throws IOException {
        String[] input = br.readLine().split(" ");
        int n = stoi(input[0]), m = stoi(input[1]);
        int[] arr = new int[n];
        for(int i = 1; i <= n; i++){
            arr[i-1] = i;
        }
        dfs(0, 0, new int[m], arr, m, n);
        bw.flush();
        bw.close();
    }
}