//BOJ10816 숫자 카드2 20210616
import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

public class BOJ10816 {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        for(String s : br.readLine().split(" ")){
            int v = Integer.parseInt(s);
            if(map.containsKey(v)){
                map.put(v, map.get(v) + 1);
            }
            else{
                map.put(v, 1);
            }
        }
        int m = Integer.parseInt(br.readLine());
        List<Integer> ans = Arrays.stream(br.readLine().split(" "))
                .map(x -> map.getOrDefault(Integer.parseInt(x), 0))
                .collect(Collectors.toList());
        for (Integer v : ans) {
            bw.write(v + " ");
        }
        bw.flush();
        bw.close();
    }
}