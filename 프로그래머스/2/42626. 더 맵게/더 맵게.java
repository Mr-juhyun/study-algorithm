import java.util.PriorityQueue;
class Solution {
    public int solution(int[] scoville, int K) {
        PriorityQueue<Integer> q = new PriorityQueue<>();
        int answer = 0;
        for(int s : scoville){
            q.offer(s);
        }
     do {   
         if (q.peek() >= K){
                break;
        }
        int least = q.poll();
        int secondLeast = q.poll();
        int newSco = least + secondLeast*2;

        q.offer(newSco);

        answer ++;
        }
        while(q.size() > 1);
        
        if (q.peek() < K){
            return -1;
        }
        return answer;
    }
}
