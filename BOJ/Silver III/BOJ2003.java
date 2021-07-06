//BOJ2003 수들의 합2 20210706
import java.io.*;
import java.util.*;

public class Main {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {
        StringTokenizer stk = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(stk.nextToken());
        int m = Integer.parseInt(stk.nextToken());
        int[] arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();


        int l = 0, r = 0;
        int sum = 0, ans = 0;
        while(true){
            if(r == n && sum < m) break;
            if(sum < m){
                sum += arr[r];
                r++;
            }else{
                sum -= arr[l];
                l++;
            }
            if(sum == m) ans++;
        }
        System.out.println(ans);
    }
}