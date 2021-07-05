//BOJ1920 수 찾기 20210705
import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

public class Main {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    
    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());
        Set<Integer> numbers = Arrays.stream(br.readLine().split(" ")).map(Integer::parseInt).collect(Collectors.toSet());
        int m = Integer.parseInt(br.readLine());
        StringTokenizer stk = new StringTokenizer(br.readLine());
        while(stk.hasMoreTokens()){
            int v = Integer.parseInt(stk.nextToken());
            bw.write(((numbers.contains(v))? 1 : 0) + "\n");
        }
        bw.flush();
        bw.close();
    }
}