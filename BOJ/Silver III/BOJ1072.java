//BOJ1072 게임 20210706
import java.io.*;
import java.util.*;

import static java.lang.Math.*;

public class Main {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {
        StringTokenizer stk = new StringTokenizer(br.readLine());
        long x = Long.parseLong(stk.nextToken());
        long y = Long.parseLong(stk.nextToken());
        long curZ = (100 * y) / x;

        long l = 0, r = x;
        long ans = -1;
        while(l <= r){
            long mid = (l+r) / 2;
            long expectZ = (100 * (y + mid)) / (x + mid);
            if(expectZ > curZ){
                ans = mid;
                r = mid - 1;
            }
            else{
                l = mid + 1;
            }
        }
        System.out.println(ans);
    }
}