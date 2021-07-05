//BOJ1713 후보 추천하기 20210705
import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

import static java.lang.Math.max;


public class Main {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));



    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());
        int k = Integer.parseInt(br.readLine());
        int[] arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        int[] likes = new int[101];
        Boolean[] inFrame = new Boolean[101];
        Arrays.fill(inFrame, false);


        int fillFrameCnt = 0;
        int[] frames = new int[n];
        int[] times = new int[101];
        for(int time = 0; time < k; time++){
            int cand = arr[time];
            if(inFrame[cand]){
                likes[cand]++;
            }else{
                if(fillFrameCnt < n){
                    frames[fillFrameCnt] = cand;
                    likes[cand] = 1;
                    times[cand] = time;
                    inFrame[cand] = true;
                    fillFrameCnt++;
                }
                else{
                    int deleteCand = selectDeleteCand(frames, times, likes);
                    int deleteIdx = findIdx(frames, deleteCand);

                    likes[deleteCand] = 0;
                    inFrame[deleteCand] = false;

                    frames[deleteIdx] = cand;
                    likes[cand] = 1;
                    times[cand] = time;
                    inFrame[cand] = true;
                }
            }
        }
        Arrays.sort(frames);
        for(int v: frames){
            if(v != 0)
                bw.write(v + " ");
        }
        bw.flush();
        bw.close();
    }

    private static int selectDeleteCand(int[] frames, int[] times,int[] likes) {
        int minLikes = Integer.MAX_VALUE;
        List<Integer> cands = new ArrayList<>();
        for(int cand: frames){
            if(minLikes > likes[cand]){
                minLikes = likes[cand];
                cands = new ArrayList<>(Arrays.asList(cand));
            }
            else if(minLikes == likes[cand]){
                cands.add(cand);
            }
        }
        int ret = cands.get(0);
        int minTime = times[ret];
        for(int cand: cands){
            if(minTime > times[cand]){
                ret = cand;
                minTime = times[cand];
            }
        }
        return ret;
    }

    private static int findIdx(int[]frames, int cand){
        for(int i = 0; i < frames.length; i++){
            if(frames[i] == cand){
                return i;
            }
        }
        return -1;
    }

}