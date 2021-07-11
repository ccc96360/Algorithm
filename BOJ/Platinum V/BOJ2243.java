//BOJ2243 사탕상자 20210711
import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

import static java.lang.Math.*;

public class Main {
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    private static int n;
    private static int max = 1000000;
    private static int[] tree;

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());

        tree = new int[(int) pow(2, (int) ceil(log2(max+1)) + 1)];

        for(int i = 0; i < n; i++){
            StringTokenizer stk = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(stk.nextToken());
            int b = Integer.parseInt(stk.nextToken());
            if(a == 1){
                int c = find(1, 0, max, b);
                bw.write(c + "\n");
                update(1, 0, max, c, -1);
            }else{
                int c = Integer.parseInt(stk.nextToken());
                update(1, 0, max , b, c);
            }
        }
        bw.flush();
        bw.close();
    }

    public static double log2(int n){
        return log10(n) / log10(2);
    }
    public static int find(int node, int start, int end, int rank){
        if(start == end){
            return start;
        }
        int mid = (start + end) / 2;
        if(tree[node * 2] >= rank){
            return find(node * 2, start, mid, rank);
        }
        else{
            return find(node * 2 + 1, mid + 1, end, rank - tree[node * 2]);
        }
    }
    public static void update(int node, int start, int end, int idx, int diff){
        if(idx < start || end < idx) return;
        if(start == end){
            tree[node] += diff;
            return;
        }
        int mid = (start + end) / 2;
        tree[node] += diff;
        update(node * 2, start, mid, idx, diff);
        update(node * 2 + 1, mid + 1, end, idx, diff);
    }
}