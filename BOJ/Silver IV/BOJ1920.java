//BOJ1920 수 찾기 20210612
import java.io.*;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.stream.Collectors;

public class BOJ1920 {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {
        HashSet<String> set;
        int n = Integer.parseInt(br.readLine());
        set = (HashSet<String>) Arrays.stream(br.readLine().split(" ")).collect(Collectors.toSet());
        int m = Integer.parseInt(br.readLine());
        List<String> arr = Arrays.stream(br.readLine().split(" ")).collect(Collectors.toList());
        for(String s: arr){
            int x = (set.contains(s)) ? 1 : 0;
            bw.write(x + "\n");
        }
        bw.flush();
        bw.close();
    }
}
