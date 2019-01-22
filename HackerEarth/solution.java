import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.HashMap;




public class solution {


public static void main(String args[]) throws IOException{
InputReader in=new InputReader(System.in);
PrintWriter out=new PrintWriter(System.out);
int T=in.readInt();

while(T-->0){
long N=in.readLong();
long min=222222222;
long minnum=0;
while(N-->0){
long num=in.readCount();
long count=in.getcount();
if(count<min){
min=count;
minnum=num;
}
}
out.println(minnum);
out.flush();

}

out.close();

}
}

class InputReader{
InputStream in;
int[] segment={6,2,5,5,4,5,6,3,7,6};
long count=0;
InputReader(InputStream in){
this.in=in;
}

public long getcount(){
return count;
}
private int read() throws IOException{
return in.read();
}



public char readChar() throws IOException{
int n=read();
while(isWhiteSpace(n)){
n=read();
}
return (char)n;
}

public int readInt() throws IOException{
int number=0;
int n=read();
while(isWhiteSpace(n)){
n=read();
}
while(!isWhiteSpace(n)){
int integer=n-'0';
number*=10;
number+=integer;
n=read();
}
return number;
}

public long readCount() throws IOException{
long number=0;
count=0;
int n=read();
while(isWhiteSpace(n)){
n=read();
}
while(!isWhiteSpace(n)){
int integer=n-'0';
count+=segment[integer];
number*=10;
number+=integer;
n=read();
}
return number;
}


public long readLong() throws IOException{
long number=0;
int n=read();
while(isWhiteSpace(n)){
n=read();
}
while(!isWhiteSpace(n)){
int integer=n-'0';
number*=10;
number+=integer;
n=read();
}
return number;
}

private boolean isWhiteSpace(int n){
if(n=='\n'||n=='\r'||n=='\t'||n==' '||n==-1){
return true;
}else{
return false;
}

}
}

