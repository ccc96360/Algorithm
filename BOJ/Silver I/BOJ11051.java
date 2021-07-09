//BOJ11051 이항 계수 2 20210709
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

        int[][] combination = new int[1001][1001];
        for(int i = 1; i <= 1000; i++){
            combination[i][0] = combination[i][i] = 1;
            for(int j = 1; j < i; j++){
                combination[i][j] = (combination[i-1][j-1] + combination[i-1][j]) % 10007;
            }
        }
        System.out.println(combination[n][k]);
    }
}