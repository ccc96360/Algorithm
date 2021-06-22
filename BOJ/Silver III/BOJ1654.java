//BOJ1654 랜선 자르기 20210622
import java.io.*;
import java.util.*;

import static java.lang.Math.max;

public class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));


    public static void main(String[] args) throws IOException {
        StringTokenizer stk = new StringTokenizer(br.readLine());
        int k = Integer.parseInt(stk.nextToken());
        int n = Integer.parseInt(stk.nextToken());

        int[] arr = new int[k];
        for(int i = 0; i < k; i++){
            arr[i] = Integer.parseInt(br.readLine());
        }

        long l = 1;
        long r = Integer.MAX_VALUE;
        long mx = -1;
        while(l <= r){
            long mid = (l + r) / 2;
            long cnt = 0;
            for(int v: arr){
                cnt += v / mid;
            }
            if(cnt >= n){
                l = mid+1;
                mx = max(mx, mid);
            }
            else{
                r = mid-1;
            }
        }
        System.out.println(mx);
    }
}