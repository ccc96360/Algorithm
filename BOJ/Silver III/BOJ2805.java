//BOJ2805 나무 자르기 20210706
import java.io.*;
import java.util.*;

import static java.lang.Math.*;

public class Main {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {
        StringTokenizer stk = new StringTokenizer(br.readLine());
        long n = Integer.parseInt(stk.nextToken());
        long m = Integer.parseInt(stk.nextToken());
        long[] arr = Arrays.stream(br.readLine().split(" ")).mapToLong(Long::parseLong).sorted().toArray();

        long ans = 0;
        long l = 0, r = arr[(int) (n-1)];
        while(l <= r){
            long mid = (l+r) / 2;
            long tmp = 0;
            for(long v: arr){
                if(v > mid) tmp += v - mid;
            }
            if(tmp >= m){
                ans = mid;
                l = mid + 1;
            }
            else{
                r = mid - 1;
            }
        }
        System.out.println(ans);
    }
}