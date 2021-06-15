//BOJ10815 숫자카드 20210615
import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

public class BOJ10815 {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());
        HashSet<Integer> set = (HashSet<Integer>) Arrays.stream(br.readLine().split(" "))
                .map(Integer::parseInt)
                .collect(Collectors.toSet());
        int m = Integer.parseInt(br.readLine());
        List<Integer> ans = Arrays.stream(br.readLine().split(" "))
                .map(x -> set.contains(Integer.parseInt(x)) ? 1 : 0)
                .collect(Collectors.toList());
        for (Integer v : ans) {
            bw.write(v + " ");
        }
        bw.flush();
        bw.close();
    }
}