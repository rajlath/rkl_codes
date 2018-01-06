import java.util.*;
import java.io.*;
public class Main {                   /////////////////////////My Solve
    static void solve() throws IOException {
                int t=In.nextInt();
	while(t-->0){
			int n=In.nextInt();
			int a[]=new int[1000001];
			long ans=0;
			//String str[]=br.readLine().split(" ");
			int mx = 0;
			for(int i=0;i<n;i++){
				int m = In.nextInt();
				a[m]++;
				if(m > mx)
					mx = m;
			}
			for(int i=mx;i>0;i--){
				int j=i;
				int count=0;
				while(j<=mx){
					if(a[j]>0){
						count+=a[j];
					}
					if(count>1){
						ans=i;
						break;
					}
					j+=i;
				}
				if(count>1)
					break;
			}
			out.println(ans);
		}
        out.close();    
    }
                   /////////////////////////My Main
    public static void main(String[] args) throws IOException {
        solve();
        out.close();
    }
                   /////////////////////////My Writer var
    public static PrintWriter out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
                       /////////////////////////My Reader Class
    private static class In {
        private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        private static StringTokenizer st = null;
        static String next() throws IOException {
            while(st == null || !st.hasMoreElements()){
                st = new StringTokenizer(br.readLine());
            }
            return st.nextToken();
        }
        static int nextInt() throws IOException{
            return Integer.parseInt(next());
        }
        static double nextDouble() throws IOException{
            return Double.parseDouble(next());
        }
        static float nextFloat() throws IOException{
            return Float.parseFloat(next());
        }
        static long nextLong() throws IOException{
            return Long.parseLong(next());
        }
        static String nextLine() throws IOException{
            String str="";
            do{
                str=br.readLine();
            }while(str.length()==0);
            return str;
        }
    }
} 
