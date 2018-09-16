#include <cstdio>
#include <cstring>
#define MAXN 100
using namespace std;
typedef struct
{int row,col;
 bool vis;
}Place;
int N;
Place p[MAXN*MAXN+1];
Place offs[8]={{0,3,0},{0,-3,0},{3,0,0},{-3,0,0},{2,2,0},{2,-2,0},{-2,2,0},{-2,-2,0}};
void showPlace(const Place *p)
{printf("(%d, %d)",p->row,p->col);
}
void showPlaces()
{for (int i=1;i<=N*N;i++) {printf("%d:",i);showPlace(&p[i]);printf(" ");}
 printf("\n");
}
bool isCorr(int i,int j)
{int diffR=p[i].row-p[j].row,diffC=p[i].col-p[j].col;
 for (int i=0;i<8;i++) if (offs[i].row==diffR && offs[i].col==diffC) return true;
 return false;
}
int check()
{
    for (int i=2;i<=N*N;i++)
    {if (p[i].vis) return 1;
     if (!isCorr(i-1,i)) return 2;
     p[i].vis=true;
    }
    if (!isCorr(N*N,1)) return 3;
    return 0;
}
int main(int cn,char **s)
{char b[512];
 FILE *f;
 f=fopen(s[1],"r");//s[1] - in-file
 if (!f){fprintf(stderr,"In-file %s not found\n",s[1]); return 0;}
 fscanf(f,"%d",&N);
 fclose(f);
 //s[2] - sol-file not needed here
 f=fopen(s[3],"r");//s[3] - result file
 if (!f){printf("0\nResult not found\n"); return 0;}
 if (N<5)
 {fscanf(f,"%s",b);
  if (strcmp(b,"NO")) printf("0\nIncorrect output\n");
  else printf("1\nCorrect\n");
  fclose(f);
  return 0;
 }
 for (int r=0;r<N;r++)
    for (int c=0;c<N;c++)
 {if (feof(f)){printf("0\nIncorrect output format\n");
               fclose(f);
               return 0;
              }
  int k;
  fscanf(f,"%d",&k);
  if (k<1 || k>N*N){printf("0\nIncorrect output value\n");
                    fclose(f);
                    return 0;
                   }
  p[k].row=r;
  p[k].col=c;
  p[k].vis=false;
 }
 fclose(f);
 switch (check())
 {case 0:{printf("1\nCorrect\n");break;}
  case 1:{printf("0\nPlace visited twice\n");break;}
  case 2:{printf("0\nInvalid move\n");break;}
  case 3:printf("0\nIncorrect finish place\n");
 }
 return 0;
}
