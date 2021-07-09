//BOJ2904 수학은 너무 쉬워 20210709
import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

import static java.lang.Math.*;

public class Main {
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    private static int n;
    private static List<Integer> primes;

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        primes = getPrimes(1000000);
        int[] arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        List<Map<Integer, Integer>> nCount = new ArrayList<>();
        Map<Integer, Integer> allPrime = new HashMap<>();
        for(int v: arr){
            int tmp = v;
            Map<Integer, Integer> count = new HashMap<>();
            for(int prime: primes){
                while(tmp % prime == 0){
                    tmp /= prime;
                    count.put(prime, count.getOrDefault(prime, 0) + 1);
                    allPrime.put(prime, allPrime.getOrDefault(prime, 0) + 1);
                }
            }
            nCount.add(count);
        }

        int gcd = 1, ans = 0;
        for(int prime: allPrime.keySet()){
            int cnt = allPrime.get(prime);
            if(cnt >= n){
                int exp = cnt / n;
                int spare = 0, lack = 0;
                gcd *= pow(prime, exp);
                for(Map<Integer, Integer> v: nCount){
                    int nCnt = v.getOrDefault(prime, 0);
                    if(nCnt < exp){
                        lack += exp - nCnt;
                    }else if(nCnt > exp){
                        spare += v.get(prime) - exp;
                    }
                    while(spare > 0 && lack > 0){
                        spare--;
                        lack--;
                        ans++;
                    }
                }
            }
        }
        System.out.println(gcd + " " + ans);
        bw.flush();
        bw.close();
    }

    public static List<Integer> getPrimes(int maxValue){
        boolean[] isPrime = new boolean[maxValue];
        Arrays.fill(isPrime, true);
        isPrime[0] = isPrime[1] = false;
        for(int i = 2; i <= (int)pow(maxValue, 0.5); i++){
            if(!isPrime[i]) continue;
            for(int j = i+i; j < maxValue; j += i){
                isPrime[j] = false;
            }
        }
        List<Integer> primes = new ArrayList<>();
        for(int i = 2; i < maxValue; i++){
            if(isPrime[i]) primes.add(i);
        }
        return primes;
    }
}