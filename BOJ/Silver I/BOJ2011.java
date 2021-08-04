//BOJ2011 암호코드 20210804
import java.io.*;
import java.util.*;

import static java.lang.Math.*;

public class Main {
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    static String[] s;
    static int[] dp;

    public static void main(String[] args) throws IOException {
        s = br.readLine().split("");
        int size = s.length;
        dp = new int[size+1];
        dp[0] = 1;

        for(int i = 1; i <= size; i++){
            if(Integer.parseInt(s[i-1]) > 0) dp[i] = dp[i-1];
            if(i == 1) continue;
            if(canEncrypt(s[i-2] + s[i-1])){
                dp[i] += dp[i-2];
            }
            dp[i] %= 1000000;
        }

        bw.write(dp[size] + "\n");
        bw.flush();
        bw.close();
    }
    static Boolean canEncrypt(String substr){
        int v = Integer.parseInt(substr);
        return (10 <= v && v <= 26);
    }
}