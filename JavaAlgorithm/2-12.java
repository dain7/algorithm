import java.util.*;
  
public class Main {
    public int Solution(int n, int m, int[][] arr) {
        int answer = 0;
        for (int s1=1; s1<=n; s1++) {
            for (int s2=1; s2<=n; s2++) {
                int cnt = 0;
                for (int exam=0; exam<m; exam++) {
                    int p1 =0, p2 = 0;
                    for (int y=0; y<n; y++) {
                        if (arr[exam][y] == s1) p1 = y;
                        if (arr[exam][y] == s2) p2 = y;
                    }
                    if (p1 < p2) cnt ++; 
                }
                if (cnt == m) answer++;
            }
        }
        return answer;
    }

    public static void main(String[] args){
        Main T = new Main();
        Scanner in=new Scanner(System.in);
        int n = in.nextInt();
        int m = in.nextInt();

        int[][] arr = new int[m][n];

        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                arr[i][j] = in.nextInt();
            }
        }
        System.out.println(T.Solution(n, m, arr));
        return ;
    }
}