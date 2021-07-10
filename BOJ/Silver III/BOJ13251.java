//BOJ13251 조약돌 꺼내기 20210710
import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

import static java.lang.Math.*;

public class Main {
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    private static int m, k;
    private static int[] arr;

    public static void main(String[] args) throws IOException {
        m = Integer.parseInt(br.readLine());
        arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        k = Integer.parseInt(br.readLine());

        int sum = Arrays.stream(arr).sum();
        double res = 0;
        for(int v: arr){
            if(v < k) continue;
            double tmp = 1;
            for(int i = 0; i < k; i++){
                tmp *= (double) (v - i) / (double) (sum - i);
            }
            res += tmp;
        }
        System.out.println(res);
    }
}