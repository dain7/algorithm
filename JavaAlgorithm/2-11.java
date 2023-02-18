        import java.util.Scanner;

        public class Main {
        public int Solution(int n, int[][] arr) {
            int max_int = 0;
            int answer = 0;
            for (int i=0; i<n; i++) {
                int count = 0;
                for (int j=0; j<n; j++) {
                    for (int k=0; k<5; k++) {
                        if (arr[i][k] == arr[j][k]) {
                            count += 1;
                            break;
                        }
                    }
                }
                if (count > max_int) {
                    max_int = count;
                    answer = i;
                }
            }
            return answer+1;
        }

        public static void main(String[] args){
            Main T = new Main();
            Scanner in=new Scanner(System.in);
            int n = in.nextInt();
            int[][] arr = new int[n][5];
            
            for (int i=0; i<n; i++) {
                for (int j=0; j<5; j++) {
                    arr[i][j] = in.nextInt();
                }
            }
            
            System.out.println(T.Solution(n, arr));
            return ;
        }
        }