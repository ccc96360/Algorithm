//BOJ10610 30 20210708
import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

import static java.lang.Math.*;

public class Main {
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    private static int n;

    public static void main(String[] args) throws IOException {
        String in = br.readLine();
        int[] intIn = Arrays.stream(in.split("")).mapToInt(Integer::parseInt).toArray();
        int sum = Arrays.stream(intIn).sum();

        if(!(sum % 3 == 0 && in.contains("0"))){
            bw.write(-1 + "\n");
        }
        else{
            String s = Arrays.stream(intIn).mapToObj(v -> Integer.toString(v)).sorted(new Comparator<String>() {
                @Override
                public int compare(String o1, String o2) {
                    return o2.compareTo(o1);
                }
            }).collect(Collectors.joining());
            bw.write(s + "\n");
        }

        bw.flush();
        bw.close();
    }
}