//BOJ11050 이항 계수 1 20210709
import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

import static java.lang.Math.*;

public class Main {
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        StringTokenizer stk = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(stk.nextToken());
        int k = Integer.parseInt(stk.nextToken());
        System.out.println(fcto(n) / (fcto(k) * fcto(n-k)));
    }
    public static int fcto(int n){
        if(n == 1) return 1;
        if(n == 0) return 1;
        return n * fcto(n-1);
    }

}