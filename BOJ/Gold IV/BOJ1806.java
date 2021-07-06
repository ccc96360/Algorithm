//BOJ1806 부분합 20210706
import java.io.*;
import java.util.*;

import static java.lang.Math.*;

public class Main {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {
        StringTokenizer stk = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(stk.nextToken());
        int s = Integer.parseInt(stk.nextToken());
        int[] arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        int ans = Integer.MAX_VALUE;

        int l = 0, r = 0;
        int sum = 0;
        while(true){
            if(r == n && sum < s) break;
            if(sum < s){
                sum += arr[r];
                r++;
            }
            else{
                sum -= arr[l];
                l++;
                ans = min(r-l+1, ans);
            }
        }
        System.out.println(((ans == Integer.MAX_VALUE) ? 0 : ans));
    }
}