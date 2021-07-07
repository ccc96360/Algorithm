//BOJ2517 달리기 20210707
import java.io.*;
import java.util.*;

import static java.lang.Math.*;

public class Main {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    private static int n;
    private static List<int[]> arr;
    private static int[] tree;

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        arr = new ArrayList<>();
        int[] ans = new int[n];
        for(int i = 0; i < n; i++){
            ans[i] = i + 1;
            arr.add(new int[]{i, Integer.parseInt(br.readLine())});
        }
        final Comparator<int[]> comp = (a,b) -> Integer.compare(a[1], b[1]);
        Collections.sort(arr, comp);

        tree = new int[(int) pow(2, ceil(log2(n)) + 1)];

        for(int[] v: arr){
            int idx = v[0];
            ans[idx] -= find(1, 0, n-1, 0, idx-1);
            update(1, 0, n-1, idx);
        }

        for(int v : ans){
            bw.write(v + "\n");
        }
        bw.flush();
        bw.close();
    }

    public static double log2(int n){
        return log10(n) / log10(2);
    }

    public static void update(int node, int start, int end, int idx){
        if(idx < start || end < idx){
            return;
        }

        tree[node]++;
        if(start != end) {
            int mid = (start + end) / 2;
            update(node * 2, start, mid, idx);
            update(node * 2 + 1, mid + 1, end, idx);
        }
    }

    public static int find(int node, int start, int end, int left, int right){
        if(left <= start && end <= right){
            return tree[node];
        }
        if(right < start || end < left){
            return 0;
        }
        int mid = (start + end) / 2;
        int l = find(node * 2, start, mid, left, right);
        int r = find(node * 2 + 1, mid + 1, end, left, right);
        return l + r;
    }

}