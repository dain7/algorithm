import java.util.Scanner;
  
public class Main {
    public int Solution(int n) {
        int answer = 0;
        int sum=0;
        int lt=1;
        for (int rt=1; rt<=(n/2)+1; rt++) {
            sum += rt;
            if (sum == n) {
                answer += 1;
            }
            while (sum >= n) {
                sum -= lt;
                lt++;
                if (sum==n) answer += 1;
            }
        }
        return answer;
    }

    public static void main(String[] args){
        Main T = new Main();
        Scanner in=new Scanner(System.in);
        int n = in.nextInt();
        System.out.println(T.Solution(n));
        return ;
    }
}