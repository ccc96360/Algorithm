//BOJ2960 에라토스테네스의 체 20210709
import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

import static java.lang.Math.*;

public class Main {
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    private static int n;

    public static void main(String[] args) throws IOException {
        StringTokenizer stk = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(stk.nextToken());
        int k = Integer.parseInt(stk.nextToken());
        boolean[] isPrime = new boolean[n+1];
        int cnt = 0;
        for(int i = 2; i <= n; i++){
            if(isPrime[i]) continue;
            for(int j = i; j <= n; j += i){
                if(isPrime[j]) continue;
                isPrime[j] = true;
                cnt++;
                if(cnt == k){
                    System.out.println(j);
                    break;
                }
            }
            if(cnt >= k) break;
        }

    }

}