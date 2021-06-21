//BOJ15656 N과 M(7) 20210621
import java.io.*;
import java.util.*;

public class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static int stoi(String v){
        return Integer.parseInt(v);
    }

    public static void dfs(int idx, int[] selected, int[] arr, int m, int n) throws IOException {
        if(idx == m){
            for(int v: selected){
                bw.write(v + " ");
            }
            bw.write("\n");
        }
        else {
            for (int i = 0; i < n; i++) {
                selected[idx] = arr[i];
                dfs(idx + 1, selected, arr, m, n);
            }
        }
    }
    public static void main(String[] args) throws IOException {
        String[] input = br.readLine().split(" ");
        int n = stoi(input[0]), m = stoi(input[1]);
        int[] arr = new int[n];
        int idx = 0;
        for(String s: br.readLine().split(" ")){
            arr[idx] = Integer.parseInt(s);
            idx++;
        }
        Arrays.sort(arr);
        dfs(0, new int[m], arr, m, n);
        bw.flush();
        bw.close();
    }
}