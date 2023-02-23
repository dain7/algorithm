import java.util.Scanner;
  
public class Main {
    // 내 풀이 실패!!
    public int Solution(int n, int m, int[] arr) {
        int answer = 0;
        int lt=0, rt=1;

        int sum=arr[lt];
        while (lt < n) {

            if (sum == m) { 
                sum-=arr[lt];
                lt++;
                answer++;
            } else if (sum > m) {
                sum -= arr[lt];
                lt++;
            } else {
                sum += arr[rt];
                rt++;
            }
        }
        return answer;
    }

    // 선생님 풀이
    public int Solution(int n, int m, int[] arr) {
        int answer = 0, sum =0;
        int lt=0;

        for (int rt=0; rt<n; rt++) {
            sum += arr[rt];
            if (sum == m) answer += 1;
            while (sum>=m) {
                sum -= arr[lt];
                lt++;
                if (sum == m) answer += 1;
            }
        } 
        return answer;
    }


    public static void main(String[] args){
        Main T = new Main();
        Scanner in=new Scanner(System.in);
        int n = in.nextInt();
        int m = in.nextInt();
        int[] arr = new int[n];
        
        for (int i=0; i<n; i++) {
            arr[i] = in.nextInt();
        }
        
        System.out.print(T.Solution(n, m, arr));
        return ;
    }
}
