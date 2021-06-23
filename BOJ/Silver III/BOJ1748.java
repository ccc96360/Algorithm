//BOJ1748 수 이어 쓰기 1 20210623
import java.io.*;

import static java.lang.Math.pow;

public class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {
        String n = br.readLine();
        int maxNum = Integer.parseInt(n);
        int maxLength = n.length();
        long ans = 0;
        for(int i = 1; i < maxLength; i++){
            ans += 9 * pow(10, i-1) * i;
        }
        ans +=  (maxNum - pow(10, maxLength - 1) + 1) * maxLength;
        System.out.println(ans);
    }
}