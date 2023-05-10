import java.util.*;
  
public class Main {
    public int Solution(int n, int m, int[][] board, int[] moves) {
        Stack<Integer> stack = new Stack<>();
        int answer = 0;
        
        for (int move : moves) {
            for (int i=0; i<n; i++) {
                if (board[i][move-1] != 0) {
                    int target = board[i][move-1];
                    board[i][move-1] = 0;
                    if (!stack.empty() && stack.peek() == target) {
                        stack.pop();
                        answer += 2;
                    } else {
                        stack.push(target);
                    }
                    break;  
                }
                
            } 
        }
        return answer;
    }

    public static void main(String[] args){
        Main T = new Main();
        Scanner in=new Scanner(System.in);
        int n = in.nextInt();
        int[][] board = new int[n][n];

        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++) {
                board[i][j] = in.nextInt();
            }
        }

        int m = in.nextInt();
        int[] moves = new int[m];

        for (int i=0; i<m; i++) {
            moves[i] = in.nextInt();
        }
        
        System.out.println(T.Solution(n, m, board, moves));
        return ;
    }
}