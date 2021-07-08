//BOJ4358 생태학 20210708
import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

import static java.lang.Math.*;

public class Main {
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        Map<String, Float> map = new HashMap<>();
        int cnt = 0;
        while (true){
            String in = br.readLine();
            if(in == null) break;
            cnt++;
            if(map.containsKey(in)){
                map.put(in, map.get(in) + 1f);
            }
            else{
                map.put(in, 1f);
            }
        }
        float n = cnt;
        List<String> orderedKey = map.keySet().stream().sorted().collect(Collectors.toList());
        for(String key: orderedKey){
            bw.write(  key+ " " + String.format("%.4f", (map.get(key) * 100) / n) + "\n");
        }

        bw.flush();
        bw.close();
    }
}