fun main()
{
    var (n, k) = readLine()!!.split(" ").map{it.toInt()}
    var values = readLine()!!.split(" ").map{it.toInt()}.sorted()
    if(k > 0)
    {
        if(values[k] != values[k - 1])
        {
           println(values[k - 1] + 1)
        }
        else
        {
            println(-1)
        }
    }
    else
    {
        println(-1)
    }




   /*
   if(!k)
    {
        ll a=cnt[0]-1>=1?cnt[0]-1:-1;cout<<a<<endl;
    }
    else if(cnt[k]!=cnt[k-1])
        cout<<cnt[k-1]<<endl;
    else
        cout<<-1<<endl;


    */




}