import java.util.Scanner;
import java.util.*;

public class Main {
  public int[] Solution(int n, int[] scores) {
    int[] answer = new int[n];
    
    for (int i=0; i<n; i++) {
      int rank = 1;
      for (int j=0; j<n; j++) {
        if (scores[i] < scores[j]) rank++;
      }
      answer[i] =rank;
    }
    return answer;
  }
    
  public static void main(String[] args){
    Main T = new Main();
    
    Scanner in=new Scanner(System.in);
    
    int n = in.nextInt();
    int[] arr = new int[n];
    
    for (int i=0; i<n; i++) {
      arr[i] = in.nextInt();
    }
		
   	for (int i :T.Solution(n, arr)) System.out.print(i+" ");
    return ;
  }
}