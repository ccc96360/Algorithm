//BOJ1062 가르침 20210705
import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

import static java.lang.Math.max;


public class Main {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static List<Integer> words;
    private static int ans = 0, defaultAns = 0, antic;

    public static void main(String[] args) throws IOException {
        StringTokenizer stk = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(stk.nextToken());
        int k = Integer.parseInt(stk.nextToken());

        if(k < 5){
            System.out.println(0);
            return;
        }
        else if(k == 26){
            System.out.println(n);
            return;
        }

        words = new ArrayList<>();

        int selected = 0;
        selected |= 1 << ('a' - 'a');
        selected |= 1 << ('n' - 'a');
        selected |= 1 << ('t' - 'a');
        selected |= 1 << ('i' - 'a');
        selected |= 1 << ('c' - 'a');
        antic = selected;
        Set<Character> usingAlpha = new HashSet<>();
        for(int i = 0; i < n; i++){
            String tmp = br.readLine().replace("anta", "").replace("tica","");
            int alpha = 0;
            for(int j = 0; j < tmp.length(); j++){
                int v = 1 << (tmp.charAt(j) - 'a');
                alpha |= v;
                if((v & antic) == 0) {
                    usingAlpha.add(tmp.charAt(j));
                }
            }
            words.add(antic | alpha);
        }

        int size = usingAlpha.size();
        if(k-5 > size){
            System.out.println(n);
            return;
        }
        String[] a = usingAlpha.stream().map(String::valueOf).collect(Collectors.toList()).toArray(new String[size]);
        solve(k-5, 0, 0, a, usingAlpha.size());
        System.out.println(ans);
    }

    private static void solve(int r, int start, int selected, String[] usingAlpha, int size){
        if(r == 0){
            int cnt = 0;
            int selectedAlpha = selected | antic;
            for(int word: words){
                if ((word & selectedAlpha) == word) cnt++;
            }
            ans = max(cnt, ans);
            return;
        }
        for(int i = start; i < size; i++){
            int v = usingAlpha[i].charAt(0) - 'a';
            if((selected & 1 << v) == 0) {
                selected |= 1 << v;
                solve(r - 1, i + 1, selected, usingAlpha, size);
                selected &= ~(1<<v);
            }
        }
    }

}