//BOJ1427 소트인사이드 20210611
import java.io.*;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;

public class BOJ1427 {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {
        String n = br.readLine();
        List<String> arr = Arrays.asList(n.split(""));
        arr.sort(new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                return o2.compareTo(o1);
            }
        });
        String tmp = arr.stream().map(x -> String.valueOf(x)).collect(Collectors.joining());
        System.out.println(tmp);
    }
}