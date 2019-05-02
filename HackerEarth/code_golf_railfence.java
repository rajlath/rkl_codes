class code_golf_railfence
{
    class Main
    {
        static java.util.function.Function<char[], java.util.function.Consumer<Integer>> d = s->k->{int l=s.length,i=0,f=0,r=0,c=0
            var a=new char[k][l];
            for(;i++<l;a[r][c++]=1,r+=f>0?1:-1)f=r<1?1:r>k-2?0:f;
            for(r=c=0;r<k;r++)
                for(i=0;i<l;i++)
                if(a[r][i]>0)
                a[r][i]=s[c++];
                for(r=c=i=0;i++<l;
                f=r<1?1:r>k-2?0:f,r+=f>0?1:-1)
                if(a[r][c]>1)
                System.out.print(a[r][c++]);
    }


    public static void main(String[] args)
    {
            System.out.println("Deciper: ");
            decipher("FAZOBRAQXOBU",3);
            decipher("ACEGIKMOQSUWYBDFHJLNPRTVXZ",2);
            decipher("AEIMQUYBDFHJLNPRTVXZCGKOSW",3);
            decipher("AGMSYBFHLNRTXZCEIKOQUWDJPV",4);
            decipher("AIQYBHJPRXZCGKOSWDFLNTVEMU",5);
            decipher("AKUBJLTVCIMSWDHNRXEGOQYFPZ",6);
            decipher("AMYBLNXZCKOWDJPVEIQUFHRTGS",7);
            decipher("AOBNPCMQDLRZEKSYFJTXGIUWHV",8);
            decipher("AQBPRCOSDNTEMUFLVGKWHJXZIY",9);
            decipher("ASBRTCQUDPVEOWFNXGMYHLZIKJ",10);
    }



    static void decipher(String s, int k)
    {
            System.out.print(s+" (key = "+k+"):\t\t");
            d.apply(s.toCharArray()).accept(k);
            System.out.println();
    }

