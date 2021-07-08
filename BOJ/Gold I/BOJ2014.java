//BOJ2014 소수의 곱 20210708
package algorithm;

import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

import static java.lang.Math.*;

public class Main {
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static long[] arr;
    private static long[] tree;

    public static void main(String[] args) throws IOException {
        StringTokenizer stk = new StringTokenizer(br.readLine());
        int k = Integer.parseInt(stk.nextToken());
        int n = Integer.parseInt(stk.nextToken());
        long[] primes = Arrays.stream(br.readLine().split(" ")).mapToLong(Long::parseLong).toArray();

        PriorityQueue<Long> pq = new PriorityQueue<>();
        Set<Long> exist = new HashSet<>();
        for(long v : primes){
            pq.add(v);
            exist.add(v);
        }

        long mx = primes[primes.length - 1];
        for(int i = 0; i < n-1; i++){
            long v = pq.poll();
            for(long prime : primes){
                if(pq.size() > n && v * prime > mx) break;
                long nv = v * prime;
                if(!exist.contains(nv)){
                    mx = max(nv, mx);
                    exist.add(nv);
                    pq.add(nv);
                }
            }
        }
        bw.write(pq.poll() + "\n");
        bw.flush();
        bw.close();
    }
}