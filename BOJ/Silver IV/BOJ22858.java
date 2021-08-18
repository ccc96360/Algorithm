//BOJ22858 원상 복구(small) 20210818
import java.io.*;
import java.util.*;

import static java.lang.Math.*;

public class Main {
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    static int n,k;
    public static void main(String[] args) throws IOException {
        StringTokenizer stk = new StringTokenizer(br.readLine());
        n = nextInt(stk);
        k = nextInt(stk);

        int[] p = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int[] d = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        for(int j = 0; j < k; j++){
            int[] np = new int[n];
            for(int i = 0; i < n; i++){
                np[d[i]-1] = p[i];
            }
            p = np;
        }
        for(int v: p){
            bw.write(v + " ");
        }
        bw.write("\n");
        bw.flush();
        bw.close();
    }

    static int nextInt(StringTokenizer stk){
        return Integer.parseInt(stk.nextToken());
    }
}