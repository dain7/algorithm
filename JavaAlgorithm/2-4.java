import java.util.*;

// 나의 풀이   
public class Main {
  public int[] Solution(int n) {
    int[] answers = new int[n];
    answers[0] = 1;

    for (int i=1; i<n; i++) {
      if (i==1) {
        answers[i] = 1;
        continue;
      }
      answers[i] = answers[i-1]+answers[i-2];
    }
    return answers;
  }
  
  public static void main(String[] args){
    Main T = new Main();
    Scanner in=new Scanner(System.in);
    int n = in.nextInt();
    for (int i : T.Solution(n)) {
      System.out.printf(i+" ");
    }
    return ;
  }
}


