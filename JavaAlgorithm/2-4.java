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


// 1번 풀이
import java.util.*;
  
public class Main {
  public int[] Solution(int n) {
    int[] answers = new int[n];
    answers[0] = 1;
	answers[1] = 1;
    for (int i=2; i<n; i++) {
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

// 2번 풀이
import java.util.*;
  
public class Main {
  public void Solution(int n) {
    int a=1, b=1, c;
    for (inti=2; i<n; i++) {
      c=a+b;
      System.out.print(c+" ");
      a=b;
      b=c;
    }
  }git
  
  public static void main(String[] args){
    Main T = new Main();
    Scanner in=new Scanner(System.in);
    int n = in.nextInt();
    T.Solution(n)
    return ;
  }
}