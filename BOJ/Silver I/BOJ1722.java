//BOJ1722 순열의 순서 20210709
import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

import static java.lang.Math.*;

public class Main {
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    private static int n;
    private static long[] permutation = new long[21];
    private static int[] numbers;
    private static int INF = 21;


    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        permutation[0] = 1;
        for(int i = 1; i <= 20; i++){
            permutation[i] = permutation[i-1] * i; 
        }

        numbers = new int[n];
        for(int i = 0; i < n; i++){
            numbers[i] = i+1;
        }

        StringTokenizer stk = new StringTokenizer(br.readLine());
        long problem = Long.parseLong(stk.nextToken());
        
        if(problem == 1){
            problem1(Long.parseLong(stk.nextToken()));
        }else{
            int[] arr = new int[n];
            for(int i = 0; i < n; i++){
                arr[i] = Integer.parseInt(stk.nextToken());
            }
            problem2(arr);
        }

    }
    public static void problem1(long k){
        int N = n;
        int[] ans = new int[n];
        for(int i = 0; i < N; i++) {
            int nth = 1;
            long block = permutation[n] / n;
            while (k > block * nth) {
                nth++;
            }
            k -= block * (nth - 1);
            ans[i] = numbers[nth-1];
            numbers[nth-1] = INF;
            Arrays.sort(numbers);
            n -= 1;
        }
        System.out.println(Arrays.stream(ans).mapToObj(Integer::toString).collect(Collectors.joining(" ")));
    }

    public static void problem2(int[] arr){
        int N = n;
        long ans = 1;
        for(int i = 0; i < N; i++){
            int v = arr[i];
            int nth = getNth(v);
            long block = permutation[n] / n;
            ans += block * (nth - 1);
            numbers[nth - 1] = INF;
            Arrays.sort(numbers);
            n -= 1;
        }
        System.out.println(ans);
    }
    public static int getNth(int n){
        int ret = 1;
        for(int v: numbers){
            if(v == n) break;
            ret++;
        }
        return ret;
    }
}