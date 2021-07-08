//BOJ2042 구간 합 구하기 20210708
import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

import static java.lang.Math.*;

public class Main {
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static long[] arr;
    private static long[] tree;

    public static void main(String[] args) throws IOException {
        StringTokenizer stk = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(stk.nextToken());
        int m = Integer.parseInt(stk.nextToken());
        int k = Integer.parseInt(stk.nextToken());
        arr = new long[n];
        for(int i = 0; i < n; i++){
            arr[i] = Long.parseLong(br.readLine());
        }

        tree = new long[(int) pow(2, ceil(log2(n)) + 1)];
        makeSegmentTree(1, 0, n-1);

        for(int i = 0; i < m + k; i++){
            String[] cmd = br.readLine().split(" ");
            int a = Integer.parseInt(cmd[0]), b = Integer.parseInt(cmd[1]) - 1;
            if(a == 1){
                long c = Long.parseLong(cmd[2]);
                update(1, 0, n-1, b, arr[b], c);
                arr[b] = c;
            }else{
                int c = Integer.parseInt(cmd[2]);
                bw.write(getSum(1, 0, n-1, b, c-1) + "\n");
            }
        }
        bw.flush();
        bw.close();
    }

    public static double log2(int n){
        return log10(n)/log10(2);
    }

    public static long makeSegmentTree(int node, int start, int end){
        if(start == end){
            tree[node] = arr[start];
            return tree[node];
        }
        int mid = (start + end) / 2;
        long left = makeSegmentTree(node * 2, start, mid);
        long right = makeSegmentTree(node * 2 + 1, mid + 1, end);
        tree[node] = left + right;
        return tree[node];
    }

    public static void update(int node, int start, int end, int idx, long before, long after){
        if(idx < start || end < idx) return;
        if(start == end){
            tree[node] = after;
            return;
        }
        tree[node] = tree[node] - before + after;
        int mid = (start + end) / 2;
        update(node * 2, start, mid, idx, before, after);
        update(node * 2 + 1, mid+1, end, idx, before, after);
    }

    public static long getSum(int node, int start, int end, int left, int right){
        if(right < start || end < left) return 0L;
        if(left <= start && end <= right){
            return tree[node];
        }
        int mid = (start + end) / 2;
        long l = getSum(node * 2, start, mid, left, right);
        long r = getSum(node * 2 + 1, mid + 1, end, left, right);
        return l + r;
    }
}