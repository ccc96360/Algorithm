//[3차]방금그곡 2018 KAKAO BLIND RECRUITMENT 20211010
import java.util.*;

import java.util.stream.Collectors;
class Solution {
    public String solution(String m, String[] musicinfos) {
        String answer = "(None)";
        List<Music> musics = Arrays.stream(musicinfos)
            .map(Music::new)
            .collect(Collectors.toList());
        
        List<String> memory = new Music().makeMelody(m);
        int n = memory.size();
        List<Music> ansCand = new ArrayList<>();
        
        for(Music music : musics){
            List<String> melody = music.melody;
            int melodyTime = melody.size(), playTime = music.playTime;
            String start = memory.get(0);
            
            for(int time = 0; time < melodyTime; time++){
                String curMelody = melody.get(time % melodyTime);
                boolean flag = false;
                if(curMelody.equals(start)){
                    int memIdx = 0;
                    for(int i = time;  i <= playTime; i++){
                        if(memIdx == n){
                            flag = true;
                            break;
                        }
                        if(!memory.get(memIdx).equals(melody.get(i % melodyTime))) break;
                        memIdx++;
                    }   
                }
                if(flag){
                    ansCand.add(music);
                    break;
                }
            }
        }
        
        int mx = -1;
        for(Music music : ansCand){
            if(music.playTime > mx){
                answer = music.name;
                mx = music.playTime;
            }
        }
        return answer;
    }
    
    class Music{
        public int playTime;
        public String name;
        public List<String> melody;
        
        public Music(){}
        public Music(String info){
            String[] tmp = info.split(",");
            String[] start = tmp[0].split(":");
            String[] end = tmp[1].split(":");
            this.playTime =  (Integer.parseInt(end[0]) * 60 + Integer.parseInt(end[1])) 
                - (Integer.parseInt(start[0]) * 60 + Integer.parseInt(start[1]));
            name = tmp[2];
            melody = makeMelody(tmp[3]);
        }
        
        public List<String> makeMelody(String m){
            int n = m.length();
            List<String> li = new ArrayList<>();
            String[] tmp = m.split("");
            for(int i = 0; i < n - 1; i++){
                StringBuilder sb = new StringBuilder(tmp[i]);
                if(tmp[i+1].equals("#")) sb.append(tmp[++i]);
                li.add(sb.toString());
            }
            if(!tmp[n - 1].equals("#")) li.add(tmp[n-1]);
            return li;
        }
    }
}