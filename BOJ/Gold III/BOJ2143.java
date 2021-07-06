//BOJ2143 두 배열의 합 20210706
import java.io.*;
import java.util.*;

import static java.lang.Math.*;

public class Main {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {
        int t = Integer.parseInt(br.readLine());
        int n = Integer.parseInt(br.readLine());
        int[] a = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int m = Integer.parseInt(br.readLine());
        int[] b = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        List<Integer> sumA = getSubSums(a, n);
        List<Integer> sumB = getSubSums(b, m);

        Map<Integer, Integer> sumACnt = new HashMap<>();
        for(int v: sumA){
            if(sumACnt.containsKey(v)){
                sumACnt.put(v, sumACnt.get(v) + 1);
            }
            else{
                sumACnt.put(v, 1);
            }
        }
        long ans = 0;
        for(int v: sumB){
            if(sumACnt.containsKey(t-v)){
                ans += sumACnt.get(t-v);
            }
        }
        System.out.println(ans);
    }

    public static List<Integer> getSubSums(int[] arr, int size){
        List<Integer> ret = new ArrayList<>();
        for(int i = 0; i < size; i++){
            int sum = 0;
            for(int j = i; j < size; j++){
                sum+= arr[j];
                ret.add(sum);
            }
        }
        return ret;
    }
}