/**
최단거리 문제 
*/


public class Main {
    Node root;
    public int BFS(Node root) {
        Queue<Node> Q = new LinkedList<>();
        Q.offer(root);
        int L = 0;
        while(!Q.isEmpty()) {
            int len = Q.size();
            for (int i=0; i<len; i++) {
                Node cur = Q.poll();
                if(cur.lt == null && cur.rt == null) return L; // 가장 처음 발겨된 말단 노드 = 가장 짧은 경로
                if(cur.lt != null) Q.offer(cur.lt);
                if(cur.rt != null) Q.offer(cur.rt);   
            }
            L ++;
        }
        return 0;
    }
}