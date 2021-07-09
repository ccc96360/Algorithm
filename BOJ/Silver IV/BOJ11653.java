//BOJ11653 소인수분해 20210709
import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

import static java.lang.Math.*;

public class Main {
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    private static int max = 10000000;
    private static int n;

    public static void main(String[] args) throws IOException {
        boolean[] isPrimes = new boolean[10000000];
        Arrays.fill(isPrimes, true);
        isPrimes[0] = isPrimes[1] = false;
        for(int i = 2; i < (int)pow(max, 0.5); i++){
            for(int j = i+i; j < max; j += i){
                isPrimes[j] = false;
            }
        }
        List<Integer> primes = new ArrayList<>();
        for(int i = 2; i < max; i++){
            if(isPrimes[i]) primes.add(i);
        }

        int n = Integer.parseInt(br.readLine());
        List<Integer> ans = new ArrayList<>();
        for(int v : primes){
            while(n % v == 0 && n != 0){
                n /= v;
                ans.add(v);
            }
            if(n == 0) break;
        }

        for(int v: ans){
            bw.write(v + "\n");
        }
        bw.flush();
        bw.close();
    }
}