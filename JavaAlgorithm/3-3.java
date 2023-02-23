import java.util.Scanner;
  
public class Main {
    public int Solution(int n, int k, int[] arr) {
        int answer = 0;
        int cur = 0;
        // 첫번째 값
        for (int i=0; i<k; i++) {
                cur += arr[i];
        }   
        answer = cur;
        for (int i=k; i<n; i++) {
            cur = cur-arr[i-k]+arr[i];
            // answer=Math.max(answer,sum);
            if (answer < cur) answer = cur;
        }

        return answer;
    }

    public static void main(String[] args){
        Main T = new Main();

        Scanner in=new Scanner(System.in);
        int n = in.nextInt();
        int k = in.nextInt();
        int[] arr = new int[n];

        for (int i=0; i<n; i++) {
            arr[i] = in.nextInt();
        }
    
        System.out.println(T.Solution(n, k, arr));
        return ;
    }
}