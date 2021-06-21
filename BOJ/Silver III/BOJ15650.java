//BOJ15650 N과 M (2) 20210621
import java.io.*;
import java.util.*;

public class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static int stoi(String v){
        return Integer.parseInt(v);
    }

    public static void dfs(int idx, int beforIdx, int[] selected, int[] arr, HashSet<Integer> isSelected, int m, int n) throws IOException {
        if(idx == m){
            for(int v: selected){
                bw.write(v + " ");
            }
            bw.write("\n");
        }
        else {
            for (int i = beforIdx + 1; i < n; i++) {
                if(!isSelected.contains(arr[i])) {
                    selected[idx] = arr[i];
                    isSelected.add(arr[i]);
                    dfs(idx + 1, i, selected, arr, isSelected, m, n);
                    isSelected.remove(arr[i]);
                }
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
        dfs(0, -1,new int[m], arr, new HashSet<Integer>(),m, n);
        bw.flush();
        bw.close();
    }
}