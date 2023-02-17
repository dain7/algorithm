import java.util.Scanner;
  
public class Main {
    public int Solution(int n, int[][] numbers) {
        int cnt = 0;
        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};

        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++) {
                boolean isMax = true;
                int cur = numbers[i][j];
                for (int k=0; k<4; k++) {
                    int x = i+dx[k];
                    int y = j+dy[k];

                    if (x >= 0 && y >= 0 && x < n && y < n) {
                        if (cur <= numbers[x][y]) {
                            isMax = false;
                            break;
                        };
                    }
                }

                if (isMax) cnt += 1;
            }
        }
        return cnt;
    }

    public static void main(String[] args){
        Main T = new Main();
        Scanner in=new Scanner(System.in);
        int n = in.nextInt();
        int[][] numbers = new int[n][n];

        
        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++) {
                numbers[i][j] = in.nextInt();
            }
        }
        System.out.println(T.Solution(n, numbers));
        return ;
    }
}