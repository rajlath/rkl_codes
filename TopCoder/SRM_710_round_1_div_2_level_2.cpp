
# -*- coding: utf-8 -*-
# @Date    : 2019-01-25 17:12:04
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

#include<vector>
using namespace std;

class ForwardMancala{
public:
    vector <int> findMoves(vector <int> start){
        vector<int>ret;
        while(1)
        {
            int count=0,index=-1;
            for(int i=0;i<start.size();i++)
            {
                if(start[i]!=0)
                {
                    count++;
                    index=i;
                }
            }
            if(count==1)
            {
                return ret;
            }
            ret.push_back(index);
            int selected=start[index];
            start[index]=0;
            for(int i=selected;i>0;i--)
            {
                start[(index+i)%start.size()]++;
            }
        }
        return ret;
    }
};
    def findMoves(self, start):
        rets = []
        while True:
            count = 0
            index = -1
            for i in range(len(start)):
                if start[index] != 0:
                    count += 1
                    index  = i
                if count ==1:
                    return rets
        rets.append(index)
        selected = start[index]
        start[index] = 0
        for i in range(selected, -1, -1):
            start[(index+i)%len(start)]+=1
        return rets

print(ForwardMancala().findMoves([6,1,0,1]))








