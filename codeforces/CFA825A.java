import java.util.*;
public final class CFA825A{
	public static void main(String args[]){
		Scanner in=new Scanner(System.in);
		int n=in.nextInt();
		String s=in.next();
		int c=1;
		for(int i=1;i<s.length();i++){
			if(s.charAt(i)=='1')
				c++;
			if(s.charAt(i)=='0'){
				System.out.print(c);
				c=0;
			}
		}
		System.out.print(c);
	}
}
