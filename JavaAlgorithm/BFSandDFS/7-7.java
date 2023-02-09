/**
BFS
 */

 class Main {
    public void BFS(Node root) {
        Queue<List> Q = new LinkedList<>();
        Q.offer(root);
        int L=0; // level
        while(!Q.isEmpty()) {
            int len = Q.size();
            // for문이 돌면 하나의 level이 끝난 것
            for (int i=0; i<len; i++) {
                Node cur = Q.poll();
                if (cur.lt != null) Q.offer(cur.lt);
                if (cur.rt != null) Q.offer(cur.rt);   
            }
            L++;
        }
    }
 }