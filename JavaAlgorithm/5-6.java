import java.util.*;
  
public class Main {
    public int Solution(int n, int k) {
        Queue<Integer> q = new LinkedList<>();
        
        for (int i=1; i<=n; i++) {
            q.offer(i);
        }

        while (q.size() > 1) {
            for (int i=1; i<k; i++) {
                q.offer(q.poll());
            }
            q.poll();
        }

        return q.poll();
    }

    public static void main(String[] args){
        Main T = new Main();
        Scanner in=new Scanner(System.in);
        int p = in.nextInt();
        int n = in.nextInt();
        System.out.println(T.Solution(p, n));
        return ;
    }
}