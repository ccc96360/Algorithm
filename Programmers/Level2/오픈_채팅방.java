//오픈 채팅방 2019 KAKAO BLIND REQRUITMENT 20210918
import java.util.*;
import java.util.stream.Collectors;

import static java.lang.Math.*;

class Solution {

    private final String ENTER = "님이 들어왔습니다.";
    private final String LEAVE = "님이 나갔습니다.";


    public String[] solution(String[] records) {
        Map<String, String> userId = new TreeMap<>();

        Queue<String[]> chatLog = new LinkedList<>();
        for (String record : records) {
            String[] tmp = record.split(" ");
            String cmd = tmp[0], uid = tmp[1];
            if(cmd.equals("Enter")){
                String nickName = tmp[2];
                userId.put(uid, nickName);
                chatLog.add(new String[]{uid, ENTER});
            }else if(cmd.equals("Leave")){
                chatLog.add(new String[]{uid, LEAVE});
            }else if(cmd.equals("Change")){
                String nickName = tmp[2];
                userId.put(uid, nickName);
            }
        }

        int n = chatLog.size();
        String[] answer = new String[n];
        for(int i = 0; i < n; i++){
            String[] tmp = chatLog.poll();
            answer[i] = userId.get(tmp[0]) + tmp[1];
        }

        return answer;
    }
}

