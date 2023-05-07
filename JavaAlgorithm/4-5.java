import java.util.Scanner;
import java.util.*;

public class Main {
    
    public int Solution(int n, int k, int[] numbers) {
        int answer = -1;
        TreeSet<Integer> numSet = new TreeSet<>(Collections.reverseOrder());
        
        for (int i=0; i<n; i++) {
            for (int j=i+1; j<n; j++) {
                for (int m=j+1; m<n; m++) {
                    numSet.add(numbers[i]+numbers[j]+numbers[m]);
                }
            }
        }

        int cnt = 0;
        for (int x : numSet) {
            cnt++;
            if (cnt==k) return x;
        }
        return answer;
    }

    public static void main(String[] args){
        Main T = new Main();
        Scanner in=new Scanner(System.in);
        int n = in.nextInt();
        int k = in.nextInt();
        int[] numbers = new int[n];

        for (int i=0; i<n; i++) {
            numbers[i] = in.nextInt();
        }

        System.out.println(T.Solution(n, k, numbers));
        return ;
    }
}