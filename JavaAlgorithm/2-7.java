import java.util.Scanner;
import java.util.stream.IntStream;

public class Main {
  public Integer Solution(int n, int[] scores) {
    int[] answer = new int[n];
	int result = 0;
    answer[0] = scores[0];
    for (int i=1; i<n; i++) {
      if (scores[i] == 1) {
        answer[i] = answer[i-1]+1;
      } else {
        answer[i] = 0;
      }
      result += answer[i];
    }
    return result;
  }
  
  public static void main(String[] args){
    Main T = new Main();
    
    Scanner in=new Scanner(System.in);
    int n = in.nextInt();
    
    int[] scores = new int[n];
    
    for (int i=0; i<n; i++) {
      scores[i] = in.nextInt();
    }

    System.out.println(T.Solution(n, scores));
    return ;
  }
}


/** 강의 풀이 */
import java.util.Scanner;
import java.util.stream.IntStream;

public class Main {
  public Integer Solution(int n, int[] scores) {
    int cnt = 0;
	int result = 0;

    for (int i=0; i<n; i++) {
      if (scores[i] == 1) {
        cnt += 1;
        result += cnt;
      } else {
        cnt = 0;
      }
    }
    return result;
  }
  
  public static void main(String[] args){
    Main T = new Main();
    
    Scanner in=new Scanner(System.in);
    int n = in.nextInt();
    
    int[] scores = new int[n];
    
    for (int i=0; i<n; i++) {
      scores[i] = in.nextInt();
    }

    System.out.println(T.Solution(n, scores));
    return ;
  }
}