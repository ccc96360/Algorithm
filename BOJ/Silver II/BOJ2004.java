//BOJ2004 조합 0의 개수 20210617
import java.io.*;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

import static java.lang.Math.min;

public class BOJ2004 {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    private static int getXCnt(int n, int x){
        int ret = 0;
        for(long i = x; i <= n; i *= x){
            ret += n / i;
        }
        return ret;
    }
    public static void main(String[] args) throws IOException {
        List<Integer> in = Arrays.stream(br.readLine().split(" ")).map(Integer :: parseInt).collect(Collectors.toList());
        int n = in.get(0);
        int m = in.get(1);
        int cnt5 = getXCnt(n, 5) - getXCnt(m, 5) - getXCnt(n - m, 5);
        int cnt2 = getXCnt(n, 2) - getXCnt(m,2) - getXCnt(n - m,2);
        System.out.println(min(cnt2,cnt5));

    }
}