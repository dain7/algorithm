import java.util.Scanner;
  
public class Main {
  public String Solution(String word) {
    char[] chars = word.toCharArray();
    int l = 0;
    int r = chars.length-1;
    
    while ( l < r ) {
      if (!Character.isAlphabetic(chars[l])) {
        l += 1;
      } else if (!Character.isAlphabetic(chars[r])) {
        r -= 1;
      } else {
        char temp = chars[l];
        chars[l] = chars[r];
        chars[r] =  temp;
        l += 1;
        r -= 1;
      }
    }
    return String.valueOf(chars); 
  }
  
  public static void main(String[] args){
    Main T = new Main();
    Scanner in=new Scanner(System.in);
    String word = in.next();
    System.out.println(T.Solution(word));
    return ;
  }
}