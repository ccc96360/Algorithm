//BOJ1339 단어 수학 20210706
import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

import static java.lang.Math.pow;

public class Main {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine().trim());

        Map<String, Integer> weights = new HashMap<>();
        for(int i = 0; i < n; i++){
            String[] tmp = br.readLine().split("");
            int size = tmp.length;
            for(int j = 0; j < size; j ++){
                String v = tmp[j];
                int w = (int) pow(10, size-1-j);
                if(weights.containsKey(v)){
                    weights.put(v, weights.get(v) + w);
                }else{
                    weights.put(v, w);
                }
            }
        }

        final Comparator<String> comp = (a,b) -> Integer.compare(weights.get(a), weights.get(b));
        List<String> order = new ArrayList<>(weights.keySet()).stream().sorted(comp.reversed()).collect(Collectors.toList());
        int ans = 0, num = 9;
        for(String v : order){
            ans += weights.get(v) * num;
            num--;
        }
        System.out.println(ans);
        bw.flush();
        bw.close();
    }
}