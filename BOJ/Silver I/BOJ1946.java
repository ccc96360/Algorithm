//BOJ1946 신입 사원 20210804
import java.io.*;
import java.util.*;

import static java.lang.Math.*;

public class Main {
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    static int n;
    static List<int[]> scores;

    public static void main(String[] args) throws IOException {
        int tc = Integer.parseInt(br.readLine());
        while(tc -- > 0){
            solve();
        }

        bw.flush();
        bw.close();
    }

    static void solve() throws IOException{
        n = Integer.parseInt(br.readLine());
        scores = new ArrayList<>();
        for(int i = 0 ; i < n; i ++){
            StringTokenizer stk = new StringTokenizer(br.readLine());
            scores.add(new int[]{nextInt(stk), nextInt(stk)});
        }
        Comparator<int[]> comp = Comparator.comparingInt(x -> x[0]);
        Collections.sort(scores, comp);

        int cnt = 1, minRank = scores.get(0)[1];
        for(int i = 1; i < n; i++){
            int[] v = scores.get(i);
            if(v[1] < minRank){
                minRank = v[1];
                cnt++;
            }
        }
        bw.write(cnt + "\n");
    }

    static int nextInt(StringTokenizer stk){
        return Integer.parseInt(stk.nextToken());
    }
}