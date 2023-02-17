import java.util.*;
  
public class Main {
    public int Solution(int n, int[][] numbers) {
        int answer = 0;
        int col, row;

        for  (int i=0; i<n; i++) {
            col=row=0;
            for (int j=0; j<n; j++) {
                row += numbers[i][j];
                col += numbers[j][i];
            }
            answer = Math.max(answer, col);
            answer = Math.max(answer, row);
        }
        col=row=0;
        for (int i=0; i<n; i++) {
            col += numbers[i][i];
            row += numbers[i][n-i-1];
            answer = Math.max(answer, col);
            answer = Math.max(answer, row);
        }
        return answer;
    }

    public static void main(String[] args){
        Main T = new Main();
        Scanner in=new Scanner(System.in);
        int n = in.nextInt();
        int[][] numbers = new int[n][n];

        for(int i=0; i<n; i++) {
            for(int j=0; j<n; j++) {
                numbers[i][j] =  in.nextInt();
            }
        }
        System.out.println(T.Solution(n, numbers));
        return ;
    }
}