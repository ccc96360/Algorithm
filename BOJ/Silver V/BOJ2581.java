//BOJ2581 소수 20210611
import java.io.*;
import java.util.Arrays;

import static java.lang.Math.min;

public class BOJ2581 {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {
        boolean[] isPrime = new boolean[10001];
        Arrays.fill(isPrime, true);
        isPrime[0] = isPrime[1] = false;
        for(int i = 2; i <= 100; i++){
            if(!isPrime[i]) continue;
            for(int j = i*2; j <= 10000; j += i){
                isPrime[j] = false;
            }
        }

        int s = Integer.parseInt(br.readLine());
        int e = Integer.parseInt(br.readLine());

        int mn = Integer.MAX_VALUE, sum = 0;
        for(int i = s; i <= e; i++){
            if(isPrime[i]){
                mn = min(mn, i);
                sum += i;
            }
        }
        if(mn == Integer.MAX_VALUE){
            System.out.println(-1);
        }
        else{
            System.out.println(sum+"\n"+mn);
        }
    }
}