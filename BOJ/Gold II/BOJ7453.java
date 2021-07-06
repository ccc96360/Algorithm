//BOJ7453 합이 0 인 네 정수 20210706
import java.io.*;
import java.util.*;

import static java.lang.Math.*;

public class Main {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());
        int[] a = new int[n];
        int[] b = new int[n];
        int[] c = new int[n];
        int[] d = new int[n];
        for(int i = 0; i < n; i++){
            StringTokenizer stk = new StringTokenizer(br.readLine());
            a[i] = Integer.parseInt(stk.nextToken());
            b[i] = Integer.parseInt(stk.nextToken());
            c[i] = Integer.parseInt(stk.nextToken());
            d[i] = Integer.parseInt(stk.nextToken());
        }

        int[] ab = getSum(a,b,n);
        int[] cd = getSum(c,d,n);

        Arrays.sort(ab);
        Arrays.sort(cd);

        long res = 0;
        for(int v : cd){
            res += upperbound(ab, -v) - lowerbound(ab, -v);
        }
        System.out.println(res);
    }

    public static int[] getSum(int[] a, int[] b, int n){
        int[] ret = new int[n*n];
        int idx = 0;
        for(int va : a){
            for(int vb : b){
                ret[idx] = va + vb;
                idx++;
            }
        }
        return ret;
    }

    public static int lowerbound(int[] arr, int v){
        int l = 0;
        int r = arr.length;
        while(l < r){
            int mid = (l+r)/2;
            if(v <= arr[mid]){
                r = mid;
            }
            else{
                l = mid + 1;
            }
        }
        return r;
    }

    public static int upperbound(int[] arr, int v){
        int l = 0;
        int r = arr.length;
        while(l < r){
            int mid = (l+r)/2;
            if(v < arr[mid]){
                r = mid;
            }
            else{
                l = mid + 1;
            }
        }
        return r;
    }
}