//BOJ2748 피보나치 수 2 20210706
import java.io.*;
import java.util.*;

import static java.lang.Math.*;

public class Main {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {
        long[] fibo = new long[91];

        fibo[0] = 0;
        fibo[1] = 1;
        for(int i = 2; i <= 90; i++){
            fibo[i] = fibo[i-1] + fibo[i-2];
        }
        System.out.println(fibo[Integer.parseInt(br.readLine())]);

    }
}